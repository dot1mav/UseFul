__all__ = ['Base']

import mysql.connector as sql


class Base:
    def __init__(self, host: str, username: str, password: str, db_name: str, charset: str='utf8'):
        self._db = sql.connect(
            host=host,
            user=username,
            password=password,
            charset=charset)
        self.db_name = db_name
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
