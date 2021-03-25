import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
	connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO familie (valoare, detalii) VALUES (?, ?)",(123, 'cumparaturi azi'))

cur.execute("INSERT INTO familie (valoare, detalii) VALUES (?, ?)",(400, 'rata masina'))

connection.commit()
connection.close()
