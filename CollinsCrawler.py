# -*- coding:utf-8 -*-

import re
from urllib import urlopen
from bs4 import BeautifulSoup

sample_path_vegetable = 'sample/vegetable-youdao.html'
sample_path_make = 'sample/make-youdao.html'
base_url = 'http://youdao.com/w/'


# Read content from path
def read(path):
    with open(path, 'r') as file:
        return file.read()


# Fetch content from URL
def fetch(word):
    url = base_url + word
    return urlopen(url).read()


# Result
def result(word, html):
    beautiful_soup = BeautifulSoup(html, 'html.parser')
    # Fetched Collins content
    collins_content = beautiful_soup.select_one('div.collinsToggle')
    # Construct models
    # Word
    word_h4 = collins_content.find('h4')
    word_name = word_h4.find(name='span', attrs={'class': 'title'}).get_text()
    word_phonetic = word_h4.find(name='em', attrs={'class': 'phonetic'}).get_text()
    word_star = word_h4.find(name='span', attrs={'class': 'star'}).attrs['class'][1]
    word_ranks = map(lambda s: s.get_text().split(' '),
                     word_h4.find_all(name='span', attrs={'class': 'rank'}))
    word_additional = map(lambda s: s.strip(),
                          re.sub('\\(|\\)', '',
                                 word_h4.find(name='span', attrs={'class': 'additional'}).get_text())
                          .split(','))

    # print(word_name, word_phonetic, word_star, word_ranks, word_additional)

    word_types = collins_content.find_all(name='div', attrs={'class': 'wt-container'})
    for word_type in word_types:
        type_name = ''
        if len(word_types) > 1:
            type_name = word_type.find(name='div', attrs={'class': 'trans-tip'}).find('span').get_text()

        # Meaning
        type_meanings = word_type.find_all(name='div', attrs={'class': 'collinsMajorTrans'})
        for type_meaning in type_meanings:
            meaning_additional = map(lambda s: s.get('title') if s.get('title') is not None else s.get_text(),
                                     type_meaning.find_all(name='span', attrs={'class': 'additional'}))
            map(lambda s: s.clear(),
                type_meaning.find('p').find_all(name='span', attrs={'class': 'additional'}))
            meaning_description = type_meaning.find('p').get_text().strip()

            # Example
            meaning_examples = collins_content.find_all(name='div', attrs={'class': 'exampleLists'})
            for meaning_example in meaning_examples:
                sentences = meaning_example.find_all('p')
                example_english = sentences[0].get_text().strip()
                example_chinese = sentences[1].get_text().strip()
    return ''


# Look up the word
def look_up(word):
    # html = read(sample_path_make)
    html = fetch(word)
    return result(word, html)
