# -*- coding:utf-8 -*-


class Type:
    id = ''
    word_id = ''
    name = ''
    meanings = []

    def desc(self):
        name = self.name if self.name is not None else ''
        return '(\'' + self.word_id + '\', \'' + name + '\')'
