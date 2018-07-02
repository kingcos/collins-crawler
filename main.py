# -*- coding:utf-8 -*-

import CollinsCrawler

if __name__ == '__main__':
    word = 'function'
    result = CollinsCrawler.look_up(word)
    # print(result)
    for t in result.types:
        for m in t.meanings:
            for e in m.examples:
                print(e.english)
                print(e.chinese)
