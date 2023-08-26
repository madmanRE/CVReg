import sqlite3
import os
from auth.hashing_password import hash_password


def create_table():
    try:
        if not os.path.exists("users.db"):
            con = sqlite3.connect("users.db")
            cursor = con.cursor()
            cursor.execute(
                """CREATE TABLE users
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                            username TEXT,
                            hashedpassword TEXT,
                            email TEXT, 
                            photo TEXT)
                        """
            )
            con.commit()
            con.close()
            return {"message": "database has been created"}
    except Exception as e:
        return {"error": f"{e}"}


def add_u(username, hashedpassword, email, photo):
    try:
        con = sqlite3.connect("users.db")
        cursor = con.cursor()
        cursor.execute(
            """INSERT INTO users (username, hashedpassword, email, photo)
                    VALUES (?, ?, ?, ?);""",
            (username, hash_password(hashedpassword), email, photo),
        )
        con.commit()
        con.close()
        return {"message": "User has been created"}
    except Exception as e:
        return {"error": f"{e}"}


def delete_u(username, password):
    try:
        con = sqlite3.connect("users.db")
        cursor = con.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND hashedpassword = ?",
            (username, hash_password(password)),
        )
        user = cursor.fetchone()
        if user:
            cursor.execute("DELETE FROM users WHERE id=?", (user[0],))
            con.commit()
            con.close()
            return {"message": "User has been deleted"}
        else:
            con.close()
            return {"message": "User not found"}
    except Exception as e:
        return {"error": f"{e}"}


def get_user(username: str, password: str):
    try:
        con = sqlite3.connect("users.db")
        cursor = con.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND hashedpassword = ?",
            (username, password),
        )
        user = cursor.fetchone()
        con.close()
        if user:
            return user
        else:
            return "No user found"
    except Exception as e:
        return {"error": f"{e}"}
