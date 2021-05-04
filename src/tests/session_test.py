import unittest
import sqlite3
from user_mgmt.session_info import SessionInfo
from user_mgmt.register import register_user
from db_mgmt import create_db

class TestSession(unittest.TestCase):
    def setUp(self):        
        self.db_name = "test.db"
        self.db_connection = create_db(self.db_name)
        self.password = "testuser_pw"
        self.user = "testuser"
        register_user(self.user,self.password,self.db_name)

    def test_user(self):
        session = SessionInfo()
        session.set_username(self.user)
        self.assertEqual(self.user,session.get_username())

    def test_db_connection(self):
        session = SessionInfo()
        session.set_db_connection(self.db_connection)
        self.assertEqual(self.db_connection,session.get_db_connection())

    def tearDown(self):
        self.db_connection.execute("DROP TABLE Users;")
        self.db_connection.execute("DROP TABLE Cost;")
        self.db_connection.execute("DROP TABLE Revenue;")
        self.db_connection.execute("DROP TABLE Plan;")
        self.db_connection.commit()
