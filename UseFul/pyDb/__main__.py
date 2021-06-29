import dotenv

from . import DatabaseManager

dotenv.load_dotenv(dotenv.find_dotenv('.dbenv'))


class Database(DatabaseManager):
    def __init__(self):
        super(Database, self).__init__()

    def set_name(self, name):
        self.raw_query(query='insert into test (name) values (%s);', args=(name,))

    def find_name(self, name):
        data = self.fetch_one(query='select * from test where name = %s;', args=(name,))
        return data[0]

    def get_all_name(self):
        names = self.fetch_all(query='select * from test')
        return names


db = Database()
db.set_name("amin")
print('data', db.find_name("amin"))
print('all data', db.get_all_name())
