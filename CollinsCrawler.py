# -*- coding:utf-8 -*-

import re
import urllib.request

from bs4 import BeautifulSoup
from Model.Word import Word
from Model.Type import Type
from Model.Meaning import Meaning
from Model.Example import Example

sample_path_vegetable = 'sample/vegetable-youdao.html'
sample_path_make = 'sample/make-youdao.html'
base_url = 'http://youdao.com/w/'


# Read content from path
def read(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


# Fetch content from URL
def fetch(word):
    url = base_url + word
    return urllib.request.urlopen(url).read()


# Result
def result(html):
    beautiful_soup = BeautifulSoup(html, 'html.parser')
    # Fetched Collins content
    collins_content = beautiful_soup.select_one('div.collinsToggle')
    # Construct models
    # Word
    word = Word()

    word_h4 = collins_content.find('h4')
    word.name = word_h4.find(name='span', attrs={'class': 'title'}).get_text()
    word.phonetic = word_h4.find(name='em', attrs={'class': 'phonetic'}).get_text()
    word.frequency = word_h4.find(name='span', attrs={'class': 'star'}).attrs['class'][1]
    word.levels = word_h4.find(name='span', attrs={'class': 'rank'}).get_text().split(' ')
    word.additional = [s.strip()
                       for s in re.sub('\\(|\\)',
                                       '',
                                       word_h4.find(name='span',
                                                    attrs={'class': 'additional'}).get_text()).split(',')]

    # print(word_name, word_phonetic, word_star, word_ranks, word_additional)

    # Type
    word_types = collins_content.find_all(name='div', attrs={'class': 'wt-container'})
    for word_type in word_types:
        w_type = Type()
        w_type.name = word_type.find(name='div', attrs={'class': 'trans-tip'}).find('span').get_text() \
            if len(word_types) > 1 else None

        # Meaning
        type_meanings = word_type.find_all(name='div', attrs={'class': 'collinsMajorTrans'})
        w_type.meanings = []
        for type_meaning in type_meanings:
            meaning = Meaning()

            meaning.additional = [s.get('title') if s.get('title') is not None else s.get_text()
                                  for s in type_meaning.find_all(name='span', attrs={'class': 'additional'})]

            [s.clear() for s in type_meaning.find('p').find_all(name='span', attrs={'class': 'additional'})]
            meaning.description = re.sub('\s{2,}', ' ', type_meaning.find('p').get_text().strip())
            # Example
            meaning_examples = type_meaning.parent.find_all(name='div', attrs={'class': 'exampleLists'})
            meaning.examples = []
            for meaning_example in meaning_examples:
                example = Example()
                sentences = meaning_example.find_all('p')
                example.english = sentences[0].get_text().strip()
                example.chinese = sentences[1].get_text().strip()
                meaning.examples.append(example)
            w_type.meanings.append(meaning)
        word.types.append(w_type)
    return word


# Look up the word
def look_up(word):
    # html = read(sample_path_vegetable)
    html = fetch(word)
    return result(html)
