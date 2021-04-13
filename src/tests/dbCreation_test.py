import unittest
import sqlite3
from create_db import CreateDB

class TestCreatDB(unittest.TestCase):
    def setUp(self):
        self.db = CreateDB("test.db")
    
    def test_userInsert(self):
        self.db.execute("INSERT INTO Users (username, password) VALUES ('user','password');")
        self.db.commit()
        self.assertEqual("user",self.db.execute("SELECT username FROM Users;").fetchone()[0])
    
    def test_dropTestDB(self):
        self.db.execute("DROP TABLE Users;")
        self.db.commit()