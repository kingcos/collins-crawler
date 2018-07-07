# -*- coding:utf-8 -*-


class Type:
    id = ''
    word_id = ''
    name = ''
    meanings = []

    def desc(self):
        return '(\'' + self.word_id + '\', \'' + self.name + '\')'
