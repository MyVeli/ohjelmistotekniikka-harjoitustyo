import unittest
from data_service.register import register_user
from data_service.login import user_login, CredentialError
from db_mgmt import create_db

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.db_name = ":memory:"
        self.db_connection = create_db(self.db_name)
        self.password = "testuser_pw"
        self.user = "testuser"
        register_user(self.user,self.password,self.db_connection)
    
    def test_password_error(self):
        error = None
        try:
            user = user_login(self.user,"wrongpassword",self.db_connection)
        except CredentialError:
            error = "CredentialError"
        self.assertEqual(error,"CredentialError")
    
    def test_username_error(self):
        error = None
        try:
            user = user_login("wrongusername",self.password,self.db_connection)
        except CredentialError:
            error = "CredentialError"
        self.assertEqual(error,"CredentialError")

    def test_login(self):
        user = user_login(self.user,self.password,self.db_connection)
        self.assertEqual(user,self.user)

    def tearDown(self):
        self.db_connection.execute("DROP TABLE Users;")
        self.db_connection.execute("DROP TABLE Cost;")
        self.db_connection.execute("DROP TABLE Revenue;")
        self.db_connection.execute("DROP TABLE Plan;")
        self.db_connection.commit()
