import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS web_crawler")
cursor.execute("USE web_crawler")
cursor.execute("""
CREATE TABLE IF NOT EXISTS urls (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL
)
""")
print("Database initialized.")
