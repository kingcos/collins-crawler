# -*- coding:utf-8 -*-

import CollinsCrawler
from Keeper import Keeper


if __name__ == '__main__':
    # word = 'function'
    # result = CollinsCrawler.look_up(word)
    # # print(result)
    # for t in result.types:
    #     for m in t.meanings:
    #         for e in m.examples:
    #             print(e.english)
    #             print(e.chinese)

    with Keeper('localhost', 'kingcos', '1234', 'WordList') as keeper:
        keeper.create_tables()



