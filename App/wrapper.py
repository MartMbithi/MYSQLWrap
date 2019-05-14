from connections import WrapConnect
from sanitize import StatementSanitizer

from collections import namedtuple

Table = namedtuple('Table', 'table_name datatype')

bob = Table(table_name='name', datatype='varchar')
jane = Table(table_name='age', datatype='Integer')

class MySQLWrapper(object):

    def __init__(self, host, database, user, password):
        self.connection = WrapConnect().connect(host, database, user, password)
        self.table_object = StatementSanitizer()

    def create_table(self, table_name, columns):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(self.table_object.sanitize_create_table(table_name, columns))
        self.connection.commit()

    def insert_values(self, table, columns, values):
        print(self.table_object.sanitize_insert_full(table, columns, values))
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(self.table_object.sanitize_insert_full(table, columns, values))
        self.connection.commit()

    def fetch_all(self, table):
        all_records = {}
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(self.table_object.sanitize_fetch_all(table))
            all_records = cursor.fetchall()
        self.connection.commit()
        return all_records

    def fetch_limit(self, table, value):
        lim = {}
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(self.table_object.sanitize_fetch_limit(table, value))
            lim = cursor.fetchone()
        self.connection.commit()
        return lim

    def fetch_columns(self, table, columns):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(self.table_object.sannitize_fetch_columns(table, columns))
        self.connection.commit()

    def update(self, table, column, new_value, conditional_column, conditional_value):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(self.table_object.santize_update(table, column, new_value, conditional_column, conditional_value))
        self.connection.commit()

    def delete_records(self, table, conditional_column, conditional_value):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(self.table_object.sanitize_delete_records(table, conditional_column, conditional_value))
        self.connection.commit()

    def delete_table(self, table):
        print(self.table_object.sanitize_delete_table(table))
        with self.connection:
            cursor = self.connection.cursor()

            cursor.execute(self.table_object.sanitize_delete_table(table))
        self.connection.commit()
        