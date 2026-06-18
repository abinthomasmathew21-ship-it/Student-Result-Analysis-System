import sqlite3

conn = sqlite3.connect("result.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    StudentID INTEGER,
    Name TEXT,
    Python INTEGER,
    SQL INTEGER,
    Maths INTEGER,
    DS INTEGER,
    Statistics INTEGER
)
""")

print("Database and table created successfully!")

conn.commit()
conn.close()
