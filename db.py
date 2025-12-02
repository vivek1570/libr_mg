import sqlite3


def get_connection():
    return sqlite3.connect("library.db")

conn = get_connection()
cursor = conn.cursor()

# Create Books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    available INTEGER DEFAULT 1
)
""")

# Create Members table
cursor.execute("""
CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT
)
""")

# Create Transactions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    member_id INTEGER,
    issue_date TEXT,
    return_date TEXT,
    FOREIGN KEY(book_id) REFERENCES books(id),
    FOREIGN KEY(member_id) REFERENCES members(id)
)
""")

# member_id,member name,book_id currently have
cursor.execute("""
    CREATE TABLE IF NOT EXISTS members(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name text not null
               )
               """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS issued_books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    issue_date TEXT,
    return_date TEXT,
    FOREIGN KEY(member_id) REFERENCES members(id),
    FOREIGN KEY(book_id) REFERENCES books(id)
)""")

conn.commit()
conn.close()

print("Tables created!")
