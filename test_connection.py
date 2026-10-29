import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv() # reads the .env file in this folder

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)
cursor = conn.cursor(dictionary=True) # rows come back as dicts

cursor.execute("SELECT COUNT(*) AS total FROM raw_students")
print(cursor.fetchone())

# Parameterized query: MySQL uses %s as the placeholder
cursor.execute(
    "SELECT raw_id, first_name, last_name, roll_no FROM raw_students WHERE school_code = %s LIMIT %s",
    ("GPS", 5),
)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()