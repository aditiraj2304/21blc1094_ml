import sqlite3

def create_tables():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            request_count INTEGER
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
