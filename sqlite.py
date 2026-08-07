import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENT(
NAME TEXT,
CLASS TEXT,
SECTION TEXT,
MARKS INTEGER
)
""")

cursor.execute("DELETE FROM STUDENT")

students = [
    ("Krishna", "Data Science", "A", 90),
    ("Ram", "Data Science", "B", 85),
    ("Priya", "AI", "A", 95),
    ("Rahul", "AI", "C", 78)
]

cursor.executemany("INSERT INTO STUDENT VALUES(?,?,?,?)", students)

conn.commit()
conn.close()

print("Database created successfully!")