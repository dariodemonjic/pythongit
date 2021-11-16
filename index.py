import hashlib
import sqlite3
from datetime import date
con = sqlite3.connect('baza.db')

def registracija():
        ime = input("Unesi ime: ")
        email = input("Unesi email: ")
        lozinka = input("Unesi lozinku: ")
        kontakt = input("Unesi kontakt broj: ")
        today = date.today() #danasnji datum

        hash_object = hashlib.md5(lozinka.encode())
        safelozinka = hash_object.hexdigest()

        cur = con.cursor()
        
        cur.execute("INSERT INTO users VALUES (2,
                    'ime', 'email', 'safelozinka', 'kontakt', 'today')")
        con.commit()
        con.close()
        

def main():
    print("Dobrodošli u Unidu sustav!")
    print("Za prijavu upišite broj 1, za registraciju broj 2:")

    unos = 0

    while(unos!=1 and unos!=2):
        unos = int(input("Unesite broj: "))


    if(unos==2):
        registracija();

        
        
        
    if(unos==1):
        email = input("Unesi email: ")
        lozinka = input("Unesi lozinku: ")


if __name__=="__main__":
    main()
