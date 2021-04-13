import sqlite3

def CreateDB(name):
    db = sqlite3.connect(name)
    
    try:
        db.execute("SELECT * FROM Users LIMIT 1;")

    except:
        print("Table Users missing. Creating.")
        db.execute("CREATE TABLE Users (username TEXT PRIMARY KEY, password TEXT);")
        db.commit()
        print("Table Users created.")
    return db

#create_db("investmentdb.db")