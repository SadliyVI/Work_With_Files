#!/usr/bin/env python
# coding: utf-8

# In[19]:


import csv

# utf-8, cp1251
# чтение файла построчно
with open(r"files\newsafr.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        if count > 0:
            print(row[-1])
        count += 1

print(f"В этом файле {count-1} новостей")


# In[41]:


import csv

# utf-8, cp1251
# чтение файла целиком
with open(r"files\newsafr.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    news_list = list(reader)

# print(news_list[:3])   
# f = open(r"files\newsafr.csv", encoding="utf-8")
# f.close()

header = news_list.pop(0)
print(f"Заголовок csv: {header}")

for row in news_list:
    print(row[-1])

print(f"В этом файле {len(news_list)} новостей")


# In[49]:


import csv

# utf-8, cp1251
# чтение файла в словарь
with open(r"files\newsafr.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    count = 0
    for row in reader:
        print(row)
        # print(row["title"])
        # count += 1

# print(f"В этом файле {count} новостей")


# In[151]:


import csv

# настройки для программиста
csv.register_dialect("csv_comma_no_quoting", delimiter=",", quoting=csv.QUOTE_NONE, escapechar="\\")
# настройки для аналитика в экселе
csv.register_dialect("csv_semicolon_quoteall", delimiter=";", quoting=csv.QUOTE_ALL)

# запись файла
with open(r"files\newsafr.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    news_list = list(reader)

header = news_list.pop(0)

# w = write, a = append
# csv.QUOTE_MINIMAL, csv.QUOTE_ALL, csv.QUOTE_NONE
f = open(r"d:\files\result.csv", "w", encoding="cp1251", newline="")
writer = csv.writer(f, dialect="csv_semicolon_quoteall")

writer.writerow(header)
writer.writerows(news_list[:2])
f.close() 



"guid""_;id";"pubDate";"description";"link";"title"
"https://www.votpusk.ru/news.asp?msg=544347";"544347";"Mon, 17 Oct 2016 00:28 +0300";"Израильский турист погиб а еще трое получили ранения в результате автомобильной аварии в Йоханнесбурге Южная Африка Об этом сообщил 2 канал в воскресенье 16 октября Трагедия произошла когда автомобиль туристов стал участником ДТП а именно когда произошло лобовое столкновение Авария произошла всего через несколько дней после того как семья туристов в Грузии потеряла двух детей в автомобильной аварии MIGnews com";"https://www.votpusk.ru/news.asp?msg=544347 ";"Израильский турист погиб в ДТП в Африке"
# In[153]:


import csv

# запись файла
with open(r"files\result.csv", encoding="cp1251", newline="") as f:
    reader = csv.reader(f, dialect="csv_semicolon_quoteall")
    for row in reader:
        print(row)


# In[191]:


import json
from pprint import pprint

# pprint.pprint.pprint()

with open(r"files\newsafr.json", encoding="utf-8") as f:
    json_data = json.load(f)

# print(type(json_data))
pprint(json_data)

# news_list = json_data["rss"]["channel"]["items"]
# # print(news_list)

for row in news_list:
    print(row["title"])
print(f"В этом файле {len(news_list)} новостей")
    
# f = open(r"files\newsafr.json")
# f.close()


# In[215]:


import json
from pprint import pprint

with open(r"files\newsafr.json", encoding="utf-8") as f:
    json_data = json.load(f)

# print(type(json_data))
json_str = json.dumps(json_data, ensure_ascii=False)
# print(type(json_str))
# print(json_str)

json_data2 = json.loads(json_str)
print(type(json_data2))
pprint(json_data2)

# f = open(r"d:\files\result.json", "w", encoding="utf-8")
# json.dump(json_data, f, ensure_ascii=False, indent=2)
# f.close()

# with open(r"d:\files\result.json", encoding="utf-8") as f:
#     json_data2 = json.load(f)

# pprint(json_data2)


# In[245]:


import xml.etree.ElementTree as ET

# создаем парсер и читаем файл в дерево XML
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse(r"files/newsafr.xml", parser)
print(tree)

root = tree.getroot()
print(root)
print(root.text)
print(root.tag)
print(root.attrib)

news_list = root.findall("channel/item")
# print(len(news_list))
# for row in news_list:
#     print(row.find("title").text)

titles_list = root.findall("channel/item/title")
for title in titles_list:
    print(title.text)

# news_list = json_data["channel"]["items"]

tree.write(r"d:\files\result.xml", encodi<rss version="2.0">
	<channel>
		<title>Новости Африка</title>
		<link>https://www.votpusk.ru/news.asp</link>
		<description>Африка - Лента туристических новостей портала В ОТПУСК.РУ </description>
		<language>ru</language>
		<category>Туризм - Африка</category>
		<lastBuildDate>Thu, 1 Dec 2016 17:27 +0300 </lastBuildDate>
		<item id="544347">
			<title>Израильский турист погиб в ДТП в Африке</title>
			<link>https://www.votpusk.ru/news.asp?msg=544347 </link>
			<description>Израильский турист погиб а еще трое получили ранения в результате автомобильной аварии в Йоханнесбурге Южная Африка Об этом сообщил 2 канал в воскресенье 16 октября Трагедия произошла когда автомобиль туристов стал участником ДТП а именно когда произошло лобовое столкновение Авария произошла всего через несколько дней после того как семья туристов в Грузии потеряла двух детей в автомобильной аварии MIGnews com</description>
			<pubDate>Mon, 17 Oct 2016 00:28 +0300</pubDate>
			<guid>https://www.votpusk.ru/news.asp?msg=544347</guid>
		</item>
ng="utf-8")

