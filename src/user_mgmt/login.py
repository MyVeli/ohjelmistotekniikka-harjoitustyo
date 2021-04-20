import hashlib
import sqlite3

def user_login(username,password,db_name):
    db_connection = sqlite3.connect(db_name)
    try:
        password_hash = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
        user_pw = db_connection.execute("SELECT password FROM Users WHERE Username = ?;",
                [username]).fetchone()
        if user_pw is None or password_hash != user_pw[0]:
            raise CredentialError("Wrong username or password")
        return username
    except ConnectionError:
        raise ConnectionError("Problem with database connection")

class CredentialError(BaseException):
    pass
