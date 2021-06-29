__all__ = ['Base']

import mysql.connector as sql
from os import environ


class Base:
    def __init__(self, host=None, username=None, password=None, db_name=None, charset='utf8'):
        self._db = sql.connect(
            host=host if host else environ['DB_HOST'],
            user=username if username else environ['DB_USER'],
            password=password if password else environ['DB_PASS'],
            charset=charset)
        self.db_name = db_name if db_name else environ['DB_NAME']
        cursor = self._db.cursor()
        self.__db_checker(cursor)
        self.__config()
        cursor.close()

    def _commit(self):
        self._db.commit()

    def __config(self):
        self._db.autocommit = True

    def __db_checker(self, cursor):
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {self.db_name};')
        self._db.database = self.db_name
        del self.db_name
