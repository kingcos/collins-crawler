# -*- coding:utf-8 -*-


class Example:
    id = ''
    meaning_id = ''
    english = ''
    chinese = ''

    def desc(self):
        return '(' + self.meaning_id + ', \'' + self.english.replace('\'', '\\\'\'') + '\', \'' + self.chinese + '\')'
