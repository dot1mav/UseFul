__all__ = ['Base']

import mysql.connector as sql

from logbook import Logger
class Base:
    def __init__(self, host: str, username: str, password: str, db_name: str, charset: str='utf8'):
        self._log = Logger('Database')
        self._db = sql.connect(
            host=host,
            user=username,
            password=password,
            charset=charset)
        cursor = self._db.cursor()
        self._log.info("create database if not exist")
        self.__db_checker(db_name,cursor)
        self._db.database = db_name
        self._log.info("enable auto commit")
        self.__config()
        cursor.close()

    def __config(self):
        self._db.autocommit = True

    def __db_checker(self, db_name, cursor):
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name};')
