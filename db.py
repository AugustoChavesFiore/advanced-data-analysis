import sys
import MySQLdb


class DB:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.db = 'companydata'
        self.connection = None
        
    def connect_DB(self):
        try:
            self.connection = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password, db=self.db)
            print('Conexión exitosa a la base de datos')
            return self.connection
        except Exception as e:
            print('Error : %s' % e)
            sys.exit(1)
    def close_DB(self):
        self.connection.close()
        return True
    
    def Query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    


