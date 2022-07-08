import sqlite3

connection = sqlite3.connect('database.db')

connection.execute('DROP TABLE IF EXISTS visitors')

connection.execute('CREATE TABLE visitors (id INTEGER PRIMARY KEY AUTOINCREMENT, created TIMESTAMP NOT NULL DEFAULT '
                   'CURRENT_TIMESTAMP, name TEXT NOT NULL, comment TEXT NOT NULL)')

cur = connection.cursor()

cur.execute("INSERT INTO visitors (name, comment) VALUES (?, ?)",
            ('Okey-Ihedi', 'My first comment')
            )

cur.execute("INSERT INTO visitors (name, comment) VALUES (?, ?)",
            ('Deborah', 'This is good')
            )

connection.commit()
connection.close()
