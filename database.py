import sqlite3
con = sqlite3.connect('baza.db')

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
               ( id INTEGER PRIMARY KEY  , name text, email text, password text, kontakt text,  created_at text)''')

cur.execute("INSERT INTO users (name, email, password, kontakt) VALUES (?,?,?,?)",('Dario',"ddemonjic8@gmail.com",'123456','0919332412'))
con.commit()


con.close()


