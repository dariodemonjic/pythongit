import hashlib
import sqlite3
import time
from datetime import date
con = sqlite3.connect('baza.db')


def login():
        ime = input("Unesi ime: ")
        lozinka = input("Unesi lozinku: ")
        hash_object = hashlib.md5(lozinka.encode())
        safelozinka = hash_object.hexdigest()
        cur = con.cursor()
        password=cur.execute("SELECT password FROM users WHERE name = ?", (ime,))
        password=cur.fetchone()
        try:
        

                if(safelozinka==password[0]):
                        login_count=cur.execute("SELECT login_count FROM users WHERE name = ?", (ime,))
                        login_count=cur.fetchone()
                        login_count=login_count[0] + 1
                        cur.execute("UPDATE users SET login_count = ? WHERE name = ?", (login_count, ime))
                        con.commit()               
                        con.close()
                        print("Uspješno ste logirani!")
                else:
                        print("Kriva lozinka.")
                
        except:
                print("Korisnik ne postoji.")


def mail():
        try:
                ime = input("Unesi ime: ")
                email = input("Unesite email: ")
                seconds = time.time()
                cur = con.cursor()
                cur.execute("INSERT INTO forgot_password (user_ime, hash) VALUES (?, ?)",(ime, seconds))
                con.commit()
                con.close()

        except:
                print("Korisnik ne postoji.")
        
def registracija():
        ime = input("Unesi ime: ")
        email = input("Unesi email: ")
        lozinka = input("Unesi lozinku: ")
        kontakt = input("Unesi kontakt broj: ")
        today = date.today() #danasnji datum

        hash_object = hashlib.md5(lozinka.encode())
        safelozinka = hash_object.hexdigest()

        cur = con.cursor()
        
        cur.execute("INSERT INTO users (name, email, password, kontakt, created_at) VALUES (?,?,?,?,?)",(ime, email, safelozinka, kontakt, today))
        con.commit()


        if(cur.rowcount>0):
                print("Podatak je zapisan")
                
        con.close()
        

def main():
    print("Dobrodošli u Unidu sustav!")
    print("Za prijavu upišite broj 1, za registraciju broj 2, a ako ste zaboravili lozinku, broj 3:")

    unos = 0

    while(unos!=1 and unos!=2 and unos!=3):
        unos = int(input("Unesite broj: "))


        if(unos==2):
                registracija()                        
                        
        if(unos==1):
                login()

        if(unos==3):
                mail()

if __name__=="__main__":
    main()
