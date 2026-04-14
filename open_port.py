#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys
import os
import re
from pathlib import Path

TARGET_USER = "tsmts"
TARGET_PORT = "ttyAP0"

def run_cmd(cmd, check=True, capture=True):
    try:
        if capture:
            result = subprocess.run(
                cmd, shell=True, check=check,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            return result.stdout.decode('utf-8').strip()
        else:
            subprocess.run(cmd, shell=True, check=check)
            return ""
    except subprocess.CalledProcessError as e:
        print("Ошибка: %s" % e)
        sys.exit(1)

def get_usb_devices():
    lsusb_out = run_cmd("lsusb")
    devices = []
    for line in lsusb_out.split('\n'):
        if 'tty' in line.lower() or 'serial' in line.lower() or 'FTDI' in line or 'CP210' in line:
            match = re.search(r'ID\s+(\w+):(\w+)', line)
            if match:
                vendor, product = match.groups()
                devices.append((vendor, product))
    return devices

def setup_user():
    print("=== Добавление пользователя '%s' в группу dialout ===" % TARGET_USER)

    check = run_cmd("id %s" % TARGET_USER, check=False)
    if not check:
        print("Ошибка: пользователь '%s' не найден!" % TARGET_USER)
        sys.exit(1)

    run_cmd("usermod -a -G dialout %s" % TARGET_USER)
    print("✓ %s добавлен в dialout" % TARGET_USER)
    print("Потребуется перелогиниться под '%s' для применения изменений." % TARGET_USER)

def create_udev_rule(devices):
    rule_file = "/etc/udev/rules.d/99-com-ports.rules"
    rules = ['# Постоянный доступ к COM-порту /dev/%s' % TARGET_PORT]

    # Правило конкретно для нашего порта
    rules.append(
        'SUBSYSTEM=="tty", KERNEL=="%s", MODE="0666", GROUP="dialout"' % TARGET_PORT
    )

    # Дополнительные правила по Vendor/Product ID если нашли устройства
    if devices:
        for vendor, product in devices:
            rule_line = 'SUBSYSTEM=="tty", ATTRS{idVendor}=="%s", ATTRS{idProduct}=="%s", MODE="0666", GROUP="dialout"' % (vendor, product)
            rules.append(rule_line)

    with open(rule_file, 'w') as f:
        f.write('\n'.join(rules) + '\n')

    run_cmd("udevadm control --reload-rules")
    run_cmd("udevadm trigger")
    print("✓ Udev-правило создано: %s" % rule_file)

def set_port_permissions():
    port_path = "/dev/%s" % TARGET_PORT
    exists = run_cmd("ls %s 2>/dev/null || echo ''" % port_path)
    if exists:
        run_cmd("chmod 666 %s" % port_path)
        print("✓ Права 666 установлены на %s (до следующей перезагрузки)" % port_path)
    else:
        print("! Порт %s сейчас не найден — права будут применены при подключении через udev." % port_path)

def check_setup():
    print("\n=== Проверка ===")
    groups_out = run_cmd("groups %s" % TARGET_USER)
    print("Группы %s: %s" % (TARGET_USER, groups_out))
    port_path = "/dev/%s" % TARGET_PORT
    port_check = run_cmd("ls -l %s 2>/dev/null || echo 'Порт %s не найден'" % (port_path, TARGET_PORT))
    print("Права %s: %s" % (port_path, port_check))
    print("✓ Настройка завершена!")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Запустите от root: sudo python3 setup_com_ports.py")
        sys.exit(1)

    print("Настройка доступа к /dev/%s для пользователя '%s'" % (TARGET_PORT, TARGET_USER))
    setup_user()

    devices = get_usb_devices()
    if devices:
        print("Обнаружены USB-устройства: %s" % str(devices))

    create_udev_rule(devices)
    set_port_permissions()

    check_setup()
    print("\nГотово! '%s' может работать с /dev/%s без sudo после перелогина." % (TARGET_USER, TARGET_PORT))