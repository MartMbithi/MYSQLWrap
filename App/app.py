from collections import namedtuple
import os 

from wrapper import MySQLWrapper
from connections import WrapConnect

host = os.getenv('SERVER_HOST')
Table = namedtuple('Table', 'table_name datatype')
bob = Table(table_name='name', datatype='VARCHAR(23)')
jane = Table(table_name='age', datatype='VARCHAR(35)')

def tab_create():
    table_creation = MySQLWrapper(host, 'tra', 'root', '')
    table_creation.create_table('fir1', [bob, jane])
    return table_creation
# tab_create()

def value_insert():
    inserted_values = MySQLWrapper(host, 'tra', 'root', '')
    inserted_values.insert_values('fir1', ['age','name'], ['90', '67'])
    return inserted_values
# value_insert()

def fetch_all():
    fecth_all_records = MySQLWrapper(host, 'tra', 'root', '')
    a = fecth_all_records.fetch_all('fir1')
    return a
b = fetch_all()
print(b)

def fetch_limit():
    fecth_limit = MySQLWrapper(host, 'tra', 'root', '')
    a = fecth_limit.fetch_limit('fir1', 1)
    return a
b = fetch_limit()
# print(b)

def fetch_specific_columns():
    pass

def table_update():
    table_updates = MySQLWrapper(host, 'tra', 'root', '')
    table_updates.update('fir1', 'age', '48', 'age', '45')
    return table_updates
# table_update()

def table_delete():
    del_table = MySQLWrapper(host, 'tra', 'root', '')
    del_table.delete_table('userlab')
    return del_table
# table_delete()