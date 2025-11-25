import urllib.request
import re
import csv
import base64

url = 'https://msk.spravker.ru/avtoservisy-avtotehcentry/'

headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')

# Очищаем скобки вокруг классов для удобства поиска
clean_html = re.sub(r'[\[\]\(\)]', '', html)

# Находим все блоки автосервисов
blocks = re.findall(r'<div class="org-widget">(.*?)</div>\s*</div>\s*</div>', clean_html, re.DOTALL)

rows = []

for block in blocks:
    # Название
    name_match = re.search(r'class="org-widget-header__title-link">([^<]+)</a>', block)
    name = name_match.group(1).strip() if name_match else ''

    # Адрес
    address_match = re.search(r'class="org-widget-header__meta org-widget-header__meta--location">([^<]+)</span>', block)
    address = address_match.group(1).strip() if address_match else ''

    # Телефоны
    phones_match = re.search(r'<dt class="spec__index"><span class="spec__index-inner">Телефон</span></dt>\s*<dd class="spec__value">([^<]+)</dd>', block)
    phones = phones_match.group(1).strip() if phones_match else ''

    # Часы работы
    hours_match = re.search(r'<dt class="spec__index"><span class="spec__index-inner">Часы работы</span></dt>\s*<dd class="spec__value">([^<]+)</dd>', block)
    hours = hours_match.group(1).strip() if hours_match else ''

    # Сайт (base64, из data-url)
    site_match = re.search(r'<span class="js-pseudo-link" data-url="([^"]+)"></span>', block)
    site_encoded = site_match.group(1).strip() if site_match else ''
    site = ''
    if site_encoded:
        try:
            site = base64.b64decode(site_encoded).decode('utf-8')
        except Exception:
            site = ''

    if name:
        rows.append([name, address, phones, hours, site])

# Запись в CSV
with open('avtoservisy.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Название', 'Адрес', 'Телефоны', 'Часы работы', 'Сайт'])
    writer.writerows(rows)

print(f'Парсинг завершён, найдено записей: {len(rows)}')
