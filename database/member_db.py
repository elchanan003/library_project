from database.db_connection import DB, db
from routes.schemas import Member

class MemberDB:
    def __init__(self, db:DB):
        self.db = db

    def create_member(self, data:Member):
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                sql = """
                INSERT INTO members(name, email, is_active, total_borrows)
                VALUES (%s, %s, True, 0)
                """
                val = (data.name, data.email)

                cur.execute(sql, val)
                conn.commit()


    def get_all_members(self):
        with self.db.connect() as conn:
            with conn.cursor(dictionary=True) as cur:
                cur.execute("""
                SELECT * FROM members
                """
                )

                data = cur.fetchall()
                return data

        

    def get_member_by_id(self, id):
        with self.db.connect() as conn:
            with conn.cursor(dictionary=True) as cur:
                sql = """
                SELECT * FROM members
                WHERE id = %s
                """
                cur.execute(sql, (id,))

                data = cur.fetchone()
                return data if data else None

    def update_member(self, id, data):
        if self.get_member_by_id(id):
            with self.db.connect() as conn:
                with conn.cursor() as cur:
                    sql = """
                    UPDATE members
                    SET name = %s, email = %s
                    WHERE id = %s              
                    """
                    val = (data.name, data.email, id)

                    cur.execute(sql, val)
                    conn.commit()

    def deactivate_member(self, id):
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                """
                UPDATE members
                SET is_active = False
                WHERE id = %s
                """,
                (id,)
                )

                conn.commit()

    def activate_member(self, id):
        with self.db.connect() as conn:
            with conn.cursor() as cur:       
                cur.execute(
                """
                UPDATE members
                SET is_active = True
                WHERE id = %s
                """,
                (id,)
                )

                conn.commit()

    def increment_borrows(self, id):
         with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                """
                UPDATE members
                SET total_borrows = total_borrows + 1
                WHERE id = %s
                """,
                (id,)
                )

                conn.commit()

    def count_active_members(self):
        with self.db.connect() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                SELECT COUNT(*) FROM members
                WHERE is_active = True
                            """)
                
                count = cur.fetchone()
                return count[0]

    def get_top_member(self):
        with self.db.connect() as conn:
            with conn.cursor(dictionary=True) as cur:
                cur.execute("""
                SELECT * FROM members
                ORDER BY total_borrows DESC
                LIMIT 1
                """)

                data = cur.fetchone()
                return data


member_db = MemberDB(db)