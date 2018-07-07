# -*- coding:utf-8 -*-

from functools import reduce


class Word:
    id = ''
    name = ''
    phonetic = ''
    frequency = ''
    additional = []
    levels = []
    types = []

    def desc(self):
        additional = reduce(lambda x, y: x + ' ' + y, self.additional) if len(self.additional) > 0 else ''
        return '(\'' + self.name + '\', \'' + self.phonetic + '\', \'' + self.frequency + '\', \'' + additional + '\')'
