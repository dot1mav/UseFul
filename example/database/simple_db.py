from UseFul.pyDb import DatabaseManager
from typing import Union


class TestDatabase(DatabaseManager):
    def __init__(self, host: str, username: str, password: str, db_name: str, charset: str = 'utf8'):
        super().__init__(host, username, password, db_name, charset=charset)

    def _create_table_person(self):
        self._raw_query(query='''create table if not exist person (name char(100));''')

    def find_name(self, name):
        if self._fetch_one(query='select * from person where name = ?', args=(name,)):
            return True
        return False

    def add_name(self, name: Union[str, list]):
        if isinstance(name, list):
            self._raw_query_many(query='', args=name)
        elif isinstance(name, str):
            self._raw_query(query='', args=(name,))


if __name__ == "__main__":
    from logbook import StreamHandler
    from sys import stdout
    StreamHandler(stdout).push_application()

    database = TestDatabase(host='localhost', username='mav',
                            password='', db_name='test_db')
    database._create_table_person()
