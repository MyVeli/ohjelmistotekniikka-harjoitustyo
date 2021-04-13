import sys, os
#dir = os.path.dirname(__file__)
import create_db
import login
#import sqlite3
import register

def main():
    dbname = "investmentdb.db"
    create_db.CreateDB(dbname)
    user = ""
    action = ""
    while (action != "l" and action != "r") or user == "":
        action = input("press l to login with existing account, r to register a new one or x to exit: ")
        if action == "l":
            user = login.Login(dbname)
        elif action == "r":
            register.Register(dbname)
            user = login.Login(dbname)
        elif action == "x":
            return True
    print(f"Welcome! You are now logged in as {user}")
    
main()