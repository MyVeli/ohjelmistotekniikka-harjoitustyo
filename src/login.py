import sqlite3
import hashlib

def Login(dbname):
    username = input("username: ")
    password = input("password: ")
    db = sqlite3.connect(dbname)
    try:
        password_hash = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
        pw = db.execute("SELECT password FROM Users WHERE Username = ?;",[username]).fetchone()
        if password_hash==pw[0]:
            return username
        return ""
    except:
        print("Wrong password")
        return ""

if __name__ == "__main__":
    Login("investmentdb.db")