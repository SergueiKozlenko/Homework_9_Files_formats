import json
import xml.etree.ElementTree as ET


def print_top_n_words(words_dict, top_int_value):
    frequency_dict = {}
    for word in words_dict:
        count = frequency_dict.get(word, 0)
        frequency_dict[word] = count + 1

    sorted_words_list = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    max_frequency_value = int(sorted_words_list[top_int_value - 1][1])
    print(f'Топ {top_int_value} самых часто встречающихся в новостях слов длиннее 6 символов:')
    for index, word_tuple in enumerate(sorted_words_list):
        if word_tuple[1] > max_frequency_value:
            print(f'{index + 1}. "{word_tuple[0]}" - {word_tuple[1]} раз')
        elif word_tuple[1] == max_frequency_value:
            print(f'{top_int_value}. "{word_tuple[0]}" - {word_tuple[1]} раз')
        else:
            break


xml_long_words = []
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
xml_items = root.findall('channel/item')
for xml_item in xml_items:
    xml_news_words = xml_item.find('description').text.split(' ')
    for xml_news_word in xml_news_words:
        if len(xml_news_word) > 6:
            xml_long_words.append(xml_news_word)

json_long_words = []
with open('newsafr.json', encoding='utf-8') as f:
    json_data = json.load(f)
    for json_item in json_data['rss']['channel']['items']:
        json_news_words = json_item['description'].split(' ')
        for json_news_word in json_news_words:
            if len(json_news_word) > 6:
                json_long_words.append(json_news_word)

print_top_n_words(xml_long_words, 10)
print_top_n_words(json_long_words, 10)
