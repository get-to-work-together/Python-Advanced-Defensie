import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS stocks
          (date text, trans text, symbol text, qty real, price real)""")

conn.commit()

c.execute("""INSERT INTO stocks 
          VALUES ('2025-01-05', 'BUY', 'IBM', 200, 392.14)""")

conn.commit()


for row in c.execute('SELECT * FROM stocks WHERE symbol = "IBM" ORDER BY price'):
     print(row)


conn.close()
