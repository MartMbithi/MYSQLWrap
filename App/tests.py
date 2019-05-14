import unittest 
from collections import namedtuple
from wrapper import MySQLWrapper

class TestWrapper(unittest.TestCase):

    def setUp(self):
        host = os.getenv('SERVER_HOST')
        connection_test = MySQLWrapper(host, 'tra', 'root', '')
        self.cursor = connection_test.cursor()
        Table = namedtuple('Table', 'table_name datatype')
        self.bob = Table(table_name='name', datatype='varchar')
        self.jane = Table(table_name='age', datatype='Integer')

    def test_create_table_successfully (self):
        self.mysqlwrapper.create_table(namedtuple('user', [self.bob, self.jane]))
        self.assertIn('user', (self.cursor.execute("Show tables;")))

    def test_create_duplicate_table(self):
        duplicate = self.mysqlwrapper.create_table(namedtuple('user', [self.bob, self.jane]))
        self.assertIn('already exists', duplicate)

    def test_insert_successfully(self):
        pass

    def test_update_successfully(self):
        pass

    def test_delete_successfully(self):
        pass

if __name__ == '__main__':
    unittest.main()