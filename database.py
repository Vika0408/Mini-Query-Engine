import sqlite3  # <-- Add this line

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        department TEXT, 
        salary INTEGER
    )
    """)
    cursor.executemany("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
                        [("Alice", "HR", 60000),
                         ("Bob", "Engineering", 80000),
                         ("Charlie", "Marketing", 50000)])
    conn.commit()
    conn.close()

def get_db_connection():
    return sqlite3.connect("database.db")
