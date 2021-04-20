import unittest
import sqlite3
from user_mgmt.register import register_user, PasswordError, UserNameError
from db_mgmt import create_db

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.db_name = "logintest.db"
        self.db_connection = create_db(self.db_name)
    
    def test_password_error(self):
        error = None
        try:
            user = register_user("testuser1","test",self.db_name)
        except PasswordError:
            error = "PasswordError"
        self.assertEqual(error,"PasswordError")
        self.assertEqual(None,self.db_connection.execute("SELECT username FROM Users;").fetchone())

    def test_registration(self):
        user = register_user("testuser","testuser_pw",self.db_name)
        user_select = self.db_connection.execute("SELECT username FROM Users;").fetchone()[0]
        self.assertEqual(user,user_select)
    
    def test_user_name_error(self):
        error = None
        user = register_user("testuser2","testuser_pw2",self.db_name)
        try:
            register_user("testuser2","testuser_pw2",self.db_name)
        except UserNameError:
            error = "UserNameError"
        self.assertEqual(error,"UserNameError")

    def tearDown(self):
        self.db_connection.execute("DROP TABLE Users;")
        self.db_connection.commit()