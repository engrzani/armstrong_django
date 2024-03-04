import sqlite3 as sql
import os

# Specify an absolute path to the database file
db_path = os.path.join(os.path.dirname(__file__), 'web_db.db')
con = sql.connect(db_path)

# Create a Connection
cur = con.cursor()

# Drop users table if it already exists.
cur.execute("DROP TABLE IF EXISTS users")

# Create users table in db_web database
user_table_sql = '''CREATE TABLE IF NOT EXISTS "users" (
    "cid" INTEGER PRIMARY KEY AUTOINCREMENT,
    "NAME" TEXT,
    "EMAIL" EMAIL,
    "CONTACT" TEXT ,
    "USERNAME" TEXT,
    "PASSWORD" TEXT
)'''
cur.execute(user_table_sql)

# Drop contact table if it already exists.
cur.execute("DROP TABLE IF EXISTS contact")

# Create contact table in db_web database
contact_table_sql = '''CREATE TABLE "contact" (
    "cid" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT,
    "email" TEXT,
    "sub" TEXT,
    "msg" TEXT
)'''
cur.execute(contact_table_sql)

# Commit changes
con.commit()

# Close the connection
con.close()
