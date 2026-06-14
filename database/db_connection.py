import mysql.connector


class DBManager:
    def __init__(self, host, user, password, database):
        self.connection = None
        self.cursor = None

        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )

        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.cursor is not None: 
            self.cursor.close()
            self.cursor = None
        if self.connection is not None:
            self.connection.close()
            self.connection = None
    
    def commit(self):
        self.connection.commit()

        
    def create_database(self):
        conn = mysql.connector.connect(
            host=self.host, 
            user=self.user, 
            password=self.password
        )

        cur = conn.cursor()

        cur.execute(f'CREATE DATABASE IF NOT EXISTS {self.database}')
        
        cur.close()
        conn.close()
        





