__all__ = ['Base', 'DatabaseManager']
__doc__ = '''
simple class to connect to Database database and check connection before all query's
'''

from .base import Base
from .manager import DataBase as DatabaseManager
