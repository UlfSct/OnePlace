import sqlite3
import random


def get_user_from_db(db, username, password):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    usr = cur.execute(
        "SELECT * FROM users LEFT JOIN userData uD ON uD.userID=users.userID WHERE username=?",
        (username,)
    ).fetchone()
    cur.close()
    conn.close()
    if usr and usr['password'] == password:
        return usr
    else:
        return None


def is_user_exists(db, username):
    is_exist = False
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    usr = cur.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
    if usr:
        is_exist = True
    cur.close()
    conn.close()
    return is_exist


def add_user_to_db(db, username, password):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    cur.execute("INSERT INTO userData (userID) VALUES (?)", str(cur.lastrowid))
    conn.commit()
    cur.close()
    conn.close()


def get_daily_tasks(db):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    tasks = cur.execute("SELECT * FROM dailyTasks").fetchall()
    random.shuffle(tasks)
    cur.close()
    conn.close()
    return tasks


def save_user_data(db, user):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(
        """UPDATE userData SET 
            money=?,
            exp=?
        WHERE userID=?""",
        tuple(map(str, [user.money, user.exp, user.userID]))
    )
    conn.commit()
    cur.close()
    conn.close()


def get_markers(db):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    markers = cur.execute("SELECT * FROM markers").fetchall()
    cur.close()
    conn.close()
    return markers
