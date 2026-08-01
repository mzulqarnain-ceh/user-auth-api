import os,sqlite3
# database setup
folder=os.path.dirname(__file__)
path=os.path.join(folder,"database.db")
def init_db():
    conn=sqlite3.connect(path)
    # conn.row_factory=sqlite3.Row
    conn.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL)")
    conn.commit()
    conn.close()
def get_db_connection():
    conn=sqlite3.connect(path)
    conn.row_factory=sqlite3.Row
    return conn
