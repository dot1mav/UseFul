__all__ = ['check_db']

from mysql.connector import DatabaseError
from functools import wraps
from typing import Union, Optional


def check_db(func):
    @wraps(func)
    def _wraps(self, query: str, args: Optional[Union[tuple, list]]=tuple(), cursor=None):
        if not self._db.is_connected():
            try:
                self._db.reconnect(attempts=5)
            except DatabaseError as de :
                self._log.error(str(de))
        if cursor is None:
            cursor = self._db.cursor(buffered=True)
        if query[-1] != ';':
            query += ';'
        self._log.info(f'QUERY={query} - ARGS={str(args)}')
        value = func(self, query, args, cursor)
        cursor.close()
        return value

    return _wraps
