import mysql.connector


class DB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        return mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
                
    def create_database(self):
        conn = mysql.connector.connect(
            host=self.host, 
            user=self.user, 
            password=self.password
        )

        with conn.cursor() as cur:
            cur.execute(f'CREATE DATABASE IF NOT EXISTS {self.database}')
        
        conn.close()
        
       
    def create_tables(self):
        with self.connect() as conn:
            with conn.cursor() as cur:

                cur.execute("""
                CREATE TABLE IF NOT EXISTS books(
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(50) NOT NULL,
                author VARCHAR(50) NOT NULL,
                genre ENUM('Fiction', 'Non-Fiction', 'Science', 'History', 'Other') NOT NULL,
                is_available BOOL NOT NULL,
                borrowed_by_member_id INT 
                )
                """)

                cur.execute("""
                CREATE TABLE IF NOT EXISTS members(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                is_active BOOL NOT NULL,
                total_borrows INT NOT NULL
                )
                """)

                

        
db = DB('localhost', 'root', 'root', 'library_db')
# db.create_database()
# db.create_tables()

        





