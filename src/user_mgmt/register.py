import hashlib
import sqlite3

def register_user(username,password,db_name):
    db_connection = sqlite3.connect(db_name)
    try:
        if db_connection.execute("SELECT password FROM Users WHERE Username = ?",
                    [username]).fetchone() is not None:
            raise UserNameError(f"username: {username} is already in use."+
            " Please select another one.")
    except ConnectionError:
        raise ConnectionError("Error with database connection")
    if len(password) < 5:
        raise PasswordError("Password needs to be 5 characters.")
    password = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
    db_connection.execute("INSERT INTO Users (username, password) VALUES (?, ?);"
                        ,[username, password])
    db_connection.commit()
    return username

class UserNameError(BaseException):
    pass

class PasswordError(BaseException):
    pass
