# -*- coding:utf-8 -*-

import pymysql


class Keeper:

    database = None
    cursor = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.database is not None:
            self.database.close()

    def __init__(self, mysql_url, username, password, database_name):
        self.database = pymysql.connect(mysql_url, username, password, database_name)
        self.cursor = self.database.cursor()

    def create_tables(self):
        sql = """CREATE TABLE IF NOT EXISTS Word (
                 id int PRIMARY KEY AUTO_INCREMENT,
                 name varchar(255) NOT NULL,
                 phonetic varchar(255),
                 frequency varchar(255),
                 additional varchar(255))"""
        self.cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Level (
                 id int PRIMARY KEY AUTO_INCREMENT,
                 wordID int,
                 name varchar(255),
                 CONSTRAINT word_rank FOREIGN KEY (wordID) REFERENCES Word (id));"""
        self.cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Type (
                 id int PRIMARY KEY AUTO_INCREMENT,
                 wordID int,
                 name varchar(255),
                 CONSTRAINT word_type FOREIGN KEY (wordID) REFERENCES Word (id));"""
        self.cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Meaning (
                 id int PRIMARY KEY AUTO_INCREMENT,
                 typeID int,
                 description varchar(255),
                 additional varchar(255),
                 CONSTRAINT type_meaning FOREIGN KEY (typeID) REFERENCES Type (id));"""
        self.cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS Example (
                 id int PRIMARY KEY AUTO_INCREMENT,
                 meaningID int,
                 english varchar(1000),
                 chinese varchar(1000),
                 CONSTRAINT meaning_example FOREIGN KEY (meaningID) REFERENCES Meaning (id));"""
        self.cursor.execute(sql)







