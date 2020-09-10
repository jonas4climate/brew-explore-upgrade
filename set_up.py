import sqlite3
conn = sqlite3.connect('db.sqlite3') # Use ':memory:' for temporary db in RAM
db = conn.cursor()

# Create table
db.execute("CREATE TABLE formulae (date text, name text)")
db.execute("CREATE TABLE casks (date text, name text)")

conn.commit()
conn.close()