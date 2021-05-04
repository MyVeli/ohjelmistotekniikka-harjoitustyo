import unittest
import sqlite3
from user_mgmt.register import register_user
from user_mgmt.login import user_login, CredentialError
from db_mgmt import create_db

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.db_name = "logintest.db"
        self.db_connection = create_db(self.db_name)
        self.password = "testuser_pw"
        self.user = "testuser"
        register_user(self.user,self.password,self.db_name)
    
    def test_password_error(self):
        error = None
        try:
            user = user_login(self.user,"wrongpassword",self.db_name)
        except CredentialError:
            error = "CredentialError"
        self.assertEqual(error,"CredentialError")
    
    def test_username_error(self):
        error = None
        try:
            user = user_login("wrongusername",self.password,self.db_name)
        except CredentialError:
            error = "CredentialError"
        self.assertEqual(error,"CredentialError")

    def test_login(self):
        user = user_login(self.user,self.password,self.db_name)
        self.assertEqual(user,self.user)

    def tearDown(self):
        self.db_connection.execute("DROP TABLE Users;")
        self.db_connection.execute("DROP TABLE Cost;")
        self.db_connection.execute("DROP TABLE Revenue;")
        self.db_connection.execute("DROP TABLE Plan;")
        self.db_connection.commit()
