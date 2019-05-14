import pymysql

class WrapConnect(object):

    def connect(self, host, database, user, password):
        # Connect to the database
        connection = pymysql.connect(host=host,
                                    database=database,
                                    user=user,
                                    password=password,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        
        return connection
    
    def commit(self, connection):
        connection.commit()

    def close(self, connection):
        connection.close()
        