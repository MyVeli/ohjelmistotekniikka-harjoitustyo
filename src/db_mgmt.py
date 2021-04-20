"""Used for initializing database and managing database tables."""

import sqlite3

def create_db(db_name):
    """Creates missing tables to db with given parameter name. Returns database connection."""
    db_connection = sqlite3.connect(db_name)
    db_connection.execute("CREATE TABLE IF NOT EXISTS Users "+
    "(username TEXT PRIMARY KEY, password TEXT);")
    db_connection.commit()
    return db_connection
