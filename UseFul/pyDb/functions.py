__all__ = ['check_db']

from functools import wraps


def check_db(func):
    @wraps(func)
    def _wraps(self, query, args=tuple(), cursor=None):
        if not self._db.is_connected():
            self._db.reconnect(attempts=5)
        if cursor is None:
            cursor = self._db.cursor(buffered=True)
        if query[-1] != ';':
            query += ';'
        value = func(self, query, args, cursor)
        cursor.close()
        return value

    return _wraps
