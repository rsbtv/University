from pymodbus.server.sync import StartSerialServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
import logging

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for p in ports:
    print(p.device, '-', p.description)

# ★ Включи логирование ★
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

slaves = {
    # 43: ModbusSlaveContext(hr=ModbusSequentialDataBlock(14200, [1,0,1,0,0])),
    # 44: ModbusSlaveContext(hr=ModbusSequentialDataBlock(1000,  [1,0,0,0,0])),
    # 45: ModbusSlaveContext(hr=ModbusSequentialDataBlock(14200, [0,1,0,1,0])),
    46: ModbusSlaveContext(hr=ModbusSequentialDataBlock(1000,  [1,0,0,0,0])),
}

context = ModbusServerContext(slaves=slaves, single=False)

print("★ Сервер запускается на COM8...")
print("★ Slave IDs: 43, 44, 45, 46")
print("★ Нажми Ctrl+C для остановки")

StartSerialServer(
    context,
    port='COM8',      # ★ убедись что это правильный порт!
    baudrate=9600,
    stopbits=1,
    bytesize=8,
    parity='N'
)
