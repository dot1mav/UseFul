__all__ = ['DataBase']

from .base import Base
from .functions import check_db


class DataBase(Base):
    def __init__(self, host: str, username: str, password: str, db_name: str, charset: str = "utf8"):
        super().__init__(host, username, password, db_name, charset=charset)

    def select(self, table, *args):
        pass

    def update(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass

    @check_db
    def raw_query(self, query: str, args: tuple = tuple(), cursor=None):
        cursor.execute(query, args)

    @check_db
    def raw_query_many(self, query: str, args: list, cursor=None):
        pass

    @check_db
    def fetch_one(self, query: str, args: tuple, cursor=None):
        cursor.execute(query, args)
        return cursor.fetchone()

    @check_db
    def fetch_all(self, query: str, args: tuple, cursor=None):
        cursor.execute(query, args)
        return cursor.fetchall()

    def close(self):
        self._db.close()
