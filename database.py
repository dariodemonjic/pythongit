import sqlite3
con = sqlite3.connect('baza.db')

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
               ( id INTEGER PRIMARY KEY AUTOINCROMENT , name text, email text, password text, kontakt text,  created_at text)''')

cur.execute("INSERT INTO users VALUES ('Dario', 'ddemonjic8@gmail.com', '12345678', '0919338417', '9.11.2021')")
con.commit()


con.close()



