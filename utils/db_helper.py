import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def update_user_request_count(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (user_id, request_count) 
        VALUES (?, 1) 
        ON CONFLICT(user_id) 
        DO UPDATE SET request_count = request_count + 1
        """, (user_id,))
    conn.commit()
    conn.close()

def get_user_request_count(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT request_count FROM users WHERE user_id = ?", (user_id,))
    row = cur.fetchone()
    conn.close()
    return row['request_count'] if row else None
