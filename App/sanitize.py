class StatementSanitizer(object):

    def sanitize_create_table(self, table_name, columns):
        statement = ''

        for column in columns:
            statement+='%s %s' % column
            statement+= ','

        sql = ''' CREATE TABLE IF NOT EXISTS {table_name} ( {statement} );''' \
                .format(table_name=table_name,statement=statement[:-1])
        
        return sql.strip()

    def sanitize_insert_full(self, table, columns,  values):

        sql = '''
        INSERT INTO {table} ({columns}) VALUES ({values});
        '''.format(table=table, columns=",".join(columns), values=",".join(values))

        return sql.strip()
    
    def sanitize_fetch_all(self, table):
        sql = ''' SELECT * FROM {table};'''.format(table=table)
        return sql.strip()

    def sanitize_fetch_limit(self, table, value):
        sql = ''' 
            SELECT * FROM {table}
            LIMIT {value}
            '''.format(table=table, value=value)

        return sql.strip()

    def sanitize_fetch_columns(self, table, columns):

        sql = '''
            SELECT {columns} FROM {table}
            '''.format(columns=','.join(columns),  table=table)

        sql.strip()

    def santize_update(self, table, column, new_value, conditional_column, conditional_value):

        sql = '''
            UPDATE {table} SET
            {column} = '{new_value}'
            WHERE {conditional_column} = '{conditional_value}'
            '''.format(table=table, column=column, new_value=new_value, conditional_column=conditional_column, conditional_value=conditional_value)

        return sql.strip()

    def sanitize_delete_records(self, table, conditional_column, conditional_value):
        sql = '''
            DELETE FROM {table}
            WHERE {conditional_column} = {conditional_value}
            '''.format(table=table, conditional_column=conditional_column, conditional_value=conditional_value) 

        return sql.strip()

    def sanitize_delete_table(self, table):
        sql = '''DROP TABLE IF EXISTS {table}'''.format(table=table)
        return sql.strip()
