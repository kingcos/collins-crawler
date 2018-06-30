# -*- coding:utf-8 -*-

from urllib import urlopen
from bs4 import BeautifulSoup

sample_path = 'sample/vegetable-youdao.html'
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
    collins_content = beautiful_soup.select_one('div.collinsToggle')
    return collins_content


# Look up the word
def look_up(word):
    # html = read(sample_path)
    html = fetch(word)
    return result(word, html)
