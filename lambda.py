import sqlite3

def handler(event, context):

    db_file = "nyc_large.db"
    print("Connecting")
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    ans = c.execute("SELECT * FROM nyc_speed LIMIT 5;")
    ans = c.fetchall()
    conn.commit()
    conn.close()

    print(ans)
    return ans