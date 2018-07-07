# -*- coding:utf-8 -*-

import CollinsCrawler
from Keeper import Keeper
from SQLiter import SQLiter


if __name__ == '__main__':
    word = 'function'
    result = CollinsCrawler.look_up(word)

    # with Keeper('localhost', 'kingcos', '1234', 'WordList') as keeper:
    #     keeper.create_tables()
    with SQLiter('WordList.db') as liter:
        liter.create_tables()
        if not liter.select('SELECT name FROM Word WHERE name = \'' + result.name + '\''):
            # Save Word
            liter.execute('INSERT INTO Word (name, phonetic, frequency, additional) values' + result.desc())
            word_id = str(liter.select('SELECT id FROM Word WHERE name = \'' + result.name + '\'')[0][0])

            # Save Level
            [liter.execute('INSERT INTO Level (wordID, name) values ('
                           + word_id + ', \'' + result.levels[0] + '\')')
             for level in result.levels]

            # Save Type
            for word_type in result.types:
                word_type.word_id = word_id
                liter.execute('INSERT INTO Type (wordID, name) values' + word_type.desc())
                type_id = str(liter.select('SELECT id FROM Type WHERE wordID = ' + word_id)[-1][0])

                # Save Meaning
                for type_meaning in word_type.meanings:
                    type_meaning.type_id = type_id

                    liter.execute('INSERT INTO Meaning (typeID, description, additional) values' + type_meaning.desc())
                    meaning_id = str(liter.select('SELECT id FROM Meaning WHERE typeID = ' + type_id + '')[-1][0])
                    # Save Example
                    for meaning_example in type_meaning.examples:
                        meaning_example.meaning_id = meaning_id
                        liter.execute('INSERT INTO Example (meaningID, english, chinese) values'
                                      + meaning_example.desc())
