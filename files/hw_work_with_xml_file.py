import xml.etree.ElementTree as ET
import collections

def read_xml(file_path, word_max_len=6, top_words_amt=10):
    """
    функция для чтения файла с новостями.
    """
    # читаем XML-документ
    tree = ET.parse(file_path)
    root = tree.getroot()

    # собираем текст новостей из слов длиннее word_max_len
    news_text = []
    for news in root.findall('channel/item'):
        description = [word for word in news.find('description').text.split(' ')
                       if len(word) > word_max_len ]
        news_text.extend(description)

    # определяем наиболее часто встречающиеся слова
    words_counter = collections.Counter(news_text)
    most_popular_words = [w[0] for w in words_counter.most_common(
        top_words_amt)]
    return most_popular_words

if __name__ == '__main__':
    print(read_xml('newsafr.xml'))


# Решение эксперта

import collections
import xml.etree.ElementTree as ET


def read_xml(file, len_word=6, top_words=10):
    tree = ET.parse(file)
    root = tree.getroot()
    xml_items = root.findall('channel/item')
    description_words = []
    descriptions = [item.find('description').text.split() for item in xml_items]
    for description in descriptions:
        description = [word for word in description if len(word) > len_word]
        description_words.extend(description)
    words_counter = collections.Counter(description_words)
    popular_words = [w[0] for w in words_counter.most_common(top_words)]
    return popular_words


if __name__ == '__main__':
    print(read_xml('newsafr.xml'))