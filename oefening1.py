import sqlite3 as sql

conn = sql.connect('./db/dummy.db')
conn.row_factory = sql.Row
rows = conn.execute('select * from students').fetchall()
print(dict(row) for row in rows)
conn.close()
