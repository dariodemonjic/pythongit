import sqlite3
con = sqlite3.connect('baza.db')

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
               ( id INTEGER PRIMARY KEY  , name text, email text, password text, kontakt text, login_count INTEGER DEFAULT 0, created_at text )''')

cur.execute('''CREATE TABLE IF NOT EXISTS forgot_password
                ( id INTEGER PRIMARY KEY, user_ime TEXT, hash TEXT, valid_until DATETIME, FOREIGN KEY (user_ime) REFERENCES users (name) )''')


con.commit()



con.close()


