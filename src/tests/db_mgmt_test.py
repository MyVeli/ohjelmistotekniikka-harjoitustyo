import unittest
import sqlite3
from db_mgmt import create_db

class TestCreateDB(unittest.TestCase):
    def setUp(self):
        self.db = create_db("dbcreatetest.db")
    
    def test_userInsert(self):
        self.db.execute("INSERT INTO Users (username, password) VALUES ('user','password');")
        self.db.commit()
        self.assertEqual("user",self.db.execute("SELECT username FROM Users;").fetchone()[0])
    
    def tearDown(self):
        self.db.execute("DROP TABLE Users;")
        self.db.commit()