import sqlite3
import hashlib

def Register(dbname):
    print("Create a new account by providing a username and password:")
    db = sqlite3.connect(dbname)
    while True:
        username = input("username: ")
        password = input("password: ")

        try:
            if db.execute("SELECT password FROM Users WHERE Username = ?",[username]).fetchone() != None:
                print(f"username: {username} is already in use. Please select another one.")
                continue
            else:
                break
        except:
            print("Something went wrong with the DB connection")
            return ""
    password = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
    db.execute("INSERT INTO Users (username, password) VALUES (?, ?);",[username, password])
    db.commit()
    print("Login with the new user account:")
    return username

if __name__ == "__main__":
    Register("investmentdb.db")