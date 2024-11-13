# Работа с файлами
# Формат CSV

# import csv
# from csv import DictReader

# utf-8, cp1251
# Чтение файла построчно

# with open('files/newsafr.csv', 'r', encoding = 'utf-8') as f:
#     reader = csv.reader(f)
#     # for line in reader:
#     #     print(line)
#     count = 0
#     for line in reader:
#         if count > 0:
#             print(f'new: {line[-1]}')
#         count += 1
# print(f'В этом файле {count} строк')

# Чтение файла целиком

# with open('files/newsafr.csv', 'r', encoding = 'utf-8') as f:
#     reader = csv.reader(f)
#     new_list = list(reader)

# header = new_list.pop(0)
# print(new_list[:5])
# print(f'Имя пользователя в колонке "{header[-1]}"')

# for row in new_list:
#     print(row)
# print(f'В этом файле {len(new_list)} строк')
#
# for row in new_list[1:]:
#     print(row)

# менеджер контекста

# f = open('files/newsafr.csv', 'r', encoding = 'utf-8')
# f.close()

# Чтение файла в словарь

# with open('files/newsafr.csv', 'r', encoding = 'utf-8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)

# Запись файла

# Диалект
# Настройки для программиста

# csv.register_dialect('csv_comma_no_quoting', delimiter = ',',
#                        quoting = csv.QUOTE_NONE, escapechar = '\\')
# # Настройки для аналитика
# csv.register_dialect('csv_semicolon_all_quoting', delimiter = ';',
#                        quoting = csv.QUOTE_ALL)
#
# with open('files/newsafr.csv', 'r', encoding = 'utf-8') as f:
#     reader = csv.reader(f)
#     new_list = list(reader)
# header = new_list.pop(0)
#
# # 'w' - write 'a' - append
# file_path = r'files\result.csv'
# with open (file_path, 'w', encoding = 'utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     # writer.writerows()
#
# with open (file_path, 'a', encoding = 'utf-8', newline = '') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#
# with open (file_path, 'a', encoding = 'utf-8', newline = '') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#
# with open (file_path, 'a', encoding = 'utf-8', newline = '') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#
# with open(file_path, 'r', encoding = 'utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#
# with open (file_path, 'a', encoding = 'utf-8', newline = '') as f:
#     writer = csv.writer(f)
#     writer.writerows(new_list)
#
# with open(file_path, 'r', encoding = 'utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#
# # csv.QUOT_MINIMAL, csv.QUOT_ALL, csv.QUOT_NOME
# with open (file_path, 'w', encoding = 'cp1251') as f:
#     writer = csv.writer(f, delimiter = ';', quoting = csv.QUOTE_MINIMAL)
#     writer.writerow(header)
#
# with open(file_path, 'r', encoding = 'utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#
# with open (file_path, 'w', encoding = 'cp1251') as f:
#     writer = csv.writer(f, delimiter = ';', quoting = csv.QUOTE_NONE,
#                         escapechar = '\\')
#     writer.writerow(header)
#
# with open (file_path, 'r', encoding = 'cp1251') as f:
#     reader = csv.reader(f, delimiter = ';', quoting = csv.QUOTE_NONE,
#                         escapechar = '\\')
#     for row in reader:
#         print(row)
#
# with open (file_path, 'r', encoding = 'cp1251') as f:
#     reader = csv.reader(f, dialect = 'csv_comma_no_quoting')
#     for row in reader:
#         print(row)

# Формат JSON

import json
from pprint import pprint

file_path_js = r'files\newfile.json'

with open(file_path_js, encoding = 'utf-8') as f:
    data = json.load(f)

# pprint(type(data))
# pprint(data)
# pprint(data['catalogs'][0]['offers'])
# f.close()

# Запись в JSON

# with open(r'files\result.json', 'w', encoding = 'utf-8') as f:
#     data = json.dump(data, f, ensure_ascii = False, indent = 2)

# with open(r'files\result.json', encoding = 'utf-8') as f:
#     data_2 = json.load(f)
# pprint(data_2)

with open(r'files\result.json', encoding = 'utf-8') as f:
    data_3 = json.load(f)
json_str = json.dumps(data_3, ensure_ascii = False)
pprint(type(json_str))
pprint(json_str)

data_4 = json.loads(json_str)
pprint(type(data_4))
pprint(data_4)

# Формат YAML

# swagger OpenAPI
# pip install pyyaml  - установка Yaml