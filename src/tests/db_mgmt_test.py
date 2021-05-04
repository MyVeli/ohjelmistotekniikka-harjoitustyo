import unittest
import sqlite3
from db_mgmt import create_db

class TestCreateDB(unittest.TestCase):
    def setUp(self):
        self.db_connection = create_db("dbcreatetest.db")
    
    def test_userInsert(self):
        self.db_connection.execute("INSERT INTO Users (username, password) VALUES ('user','password');")
        self.db_connection.commit()
        self.assertEqual("user",self.db_connection.execute("SELECT username FROM Users;").fetchone()[0])
    
    def tearDown(self):
        self.db_connection.execute("DROP TABLE Users;")
        self.db_connection.execute("DROP TABLE Cost;")
        self.db_connection.execute("DROP TABLE Revenue;")
        self.db_connection.execute("DROP TABLE Plan;")
        self.db_connection.commit()