import sqlite3


conn = sqlite3.connect('oneplace.db')

with open('schema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('Abobus', '12345')
            )

lastID = cur.lastrowid

cur.execute("INSERT INTO userData (userID) VALUES (?)", (str(lastID)))

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('_Cool_', '3221337')
            )

lastID = cur.lastrowid

cur.execute("INSERT INTO userData (userID) VALUES (?)", (str(lastID)))

conn.commit()
conn.close()
