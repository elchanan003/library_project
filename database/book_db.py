from database.db_connection import DB, db
from routes.schemas import Data

class BookDB:
    def __init__(self, db:DB):
        self.db = db

    def create_book(self, data:Data):
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                """
                INSERT INTO books(title, author, genre, is_available, borrowed_by_member_id)
                VALUES(%s, %s, %s, True, NULL)
                """,
                 (data.title, data.author, data.genre)
                )
                conn.commit()
            

    def get_all_books(self):
        with self.db.connect() as conn:
            with conn.cursor(dictionary=True) as cur:
                cur.execute(
                    """
                    SELECT * FROM books
                    """
                )
                data = cur.fetchall()
                return data
            

    def get_book_by_id(self, id):
        with self.db.connect() as conn:
            with conn.cursor(dictionary=True) as cur:
                cur.execute(
                    """
                    SELECT * FROM books
                    WHERE id = %s
                    """,
                    (id,)
                )

                data = cur.fetchone()
                return data if data else None

    def update_book(self, id, data:Data):
        if self.get_book_by_id(id):
            with self.db.connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                    """
                    UPDATE books
                    SET title = %s, author = %s, genre = %s
                    WHERE id = %s
                    """,
                        (data.title, data.author, data.genre, id)
                    )

                    conn.commit()


    def set_available(self, id, val, member_id):
        if self.get_book_by_id(id):
            with self.db.connect() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                    """
                    UPDATE books
                    SET is_available = %s, borrowed_by_member_id = %s
                    WHERE id = %s
                    """,
                    (val, member_id, id)
                    )

                    conn.commit()

    def count_total_books(self):
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                SELECT COUNT(*) FROM books
                """)
                
                data = cur.fetchone()
                return data[0]

    def count_available_books(self):
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                SELECT COUNT(*) FROM books
                WHERE is_available = True
                """)
                
                data = cur.fetchone()
                return data[0]

    def count_borrowed_books(self):
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                SELECT COUNT(*) FROM books
                WHERE is_available = False
                """)
                
                data = cur.fetchone()
                return data[0]

    def count_by_genre(self, genre):
         with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                """
                SELECT COUNT(*) FROM books
                WHERE genre = %s
                """,
                (genre,)
                )
                
                data = cur.fetchone()
                return data[0]

    def count_active_borrows_by_member(self,member_id):
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                """
                SELECT COUNT(*) FROM books
                WHERE borrowed_by_member_id = %s
                """,
                (member_id,)
                )
                
                data = cur.fetchone()
                return data[0]
        


      

