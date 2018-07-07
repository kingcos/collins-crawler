# -*- coding:utf-8 -*-

import sqlite3


class SQLiter:
    connection = None
    cursor = None

    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()

    def create_tables(self):
        sql = """CREATE TABLE IF NOT EXISTS Word (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name varchar(255),
                 phonetic varchar(255),
                 frequency varchar(255),
                 additional varchar(255))"""
        self.cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Level (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 wordID INTEGER,
                 name varchar(255),
                 CONSTRAINT word_rank FOREIGN KEY (wordID) REFERENCES Word (id));"""
        self.cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Type (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 wordID INTEGER,
                 name varchar(255),
                 CONSTRAINT word_type FOREIGN KEY (wordID) REFERENCES Word (id));"""
        self.cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Meaning (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 typeID INTEGER,
                 description varchar(255),
                 additional varchar(255),
                 CONSTRAINT type_meaning FOREIGN KEY (typeID) REFERENCES Type (id));"""
        self.cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Example (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 meaningID INTEGER,
                 english varchar(1000),
                 chinese varchar(1000),
                 CONSTRAINT meaning_example FOREIGN KEY (meaningID) REFERENCES Meaning (id));"""
        self.cursor.execute(sql)

    def execute(self, sql):
        self.cursor.execute(sql)
        self.connection.commit()

    def select(self, sql):
        self.cursor.execute(sql)
        values = self.cursor.fetchall()
        return values
