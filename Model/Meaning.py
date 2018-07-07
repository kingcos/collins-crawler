# -*- coding:utf-8 -*-

from functools import reduce


class Meaning:
    id = ''
    type_id = ''
    description = ''
    additional = []
    examples = []

    def desc(self):
        additional = reduce(lambda x, y: x + ' ' + y, self.additional) if len(self.additional) > 0 else ''
        return '(\'' + self.type_id + '\', \'' + self.description + '\', \'' + additional + '\')'
