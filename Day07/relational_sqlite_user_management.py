import sqlite3


class UserDatabaseManager:

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                address TEXT,
                mobile TEXT,
                email TEXT
            )
        """)

        self.conn.commit()

    def find_user(self, username):
        cursor = self.conn.execute(
            """
            SELECT id, username, address, mobile, email
            FROM users
            WHERE username = ?
            """,
            (username,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return {
            "id": row[0],
            "username": row[1],
            "address": row[2],
            "mobile": row[3],
            "email": row[4]
        }

    def add_or_update_user(
        self,
        username,
        address,
        mobile,
        email
    ):
        
        existing_user = self.find_user(username)

        if existing_user is not None:

            self.conn.execute(
                """
                UPDATE users
                SET address = ?,
                    mobile = ?,
                    email = ?
                WHERE username = ?
                """,
                (address, mobile, email, username)
            )

            self.conn.commit()

            return "UPDATED"

        else:

            self.conn.execute(
                """
                INSERT INTO users
                (username, address, mobile, email)
                VALUES (?, ?, ?, ?)
                """,
                (username, address, mobile, email)
            )

            self.conn.commit()

            return "INSERTED"

    def list_all_users(self):

        cursor = self.conn.execute(
            """
            SELECT id, username, address, mobile, email
            FROM users
            ORDER BY username ASC
            """
        )

        rows = cursor.fetchall()

        users = []

        for row in rows:
            users.append({
                "id": row[0],
                "username": row[1],
                "address": row[2],
                "mobile": row[3],
                "email": row[4]
            })

        return users

    def close(self):
        self.conn.close()



if __name__ == "__main__":

    db = UserDatabaseManager("company.db")

    
    status1 = db.add_or_update_user(
        "arham_k",
        "Pune, MH",
        "9876543210",
        "arham@cdac.in"
    )

    print(status1)

    user_info = db.find_user("arham_k")

    if user_info:
        print(user_info)
        print(user_info["email"])

    status2 = db.add_or_update_user(
        "arham_k",
        "Bengaluru, KA",
        "9876543210",
        "arham@cdac.in"
    )

    print(status2)

    
    users = db.list_all_users()

    for user in users:
        print(user)

    db.close()