import unittest
from data_service.register import register_user, PasswordError, UserNameError
from db_mgmt import create_db

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.db_name = ":memory:"
        self.db_connection = create_db(self.db_name)
    
    def test_password_error(self):
        error = None
        try:
            user = register_user("testuser1","test",self.db_connection)
        except PasswordError:
            error = "PasswordError"
        self.assertEqual(error,"PasswordError")
        self.assertEqual(None,self.db_connection.execute("SELECT username FROM Users;").fetchone())

    def test_registration(self):
        user = register_user("testuser","testuser_pw",self.db_connection)
        user_select = self.db_connection.execute("SELECT username FROM Users;").fetchone()[0]
        self.assertEqual(user,user_select)
    
    def test_user_name_error(self):
        error = None
        user = register_user("testuser2","testuser_pw2",self.db_connection)
        try:
            register_user("testuser2","testuser_pw2",self.db_connection)
        except UserNameError:
            error = "UserNameError"
        self.assertEqual(error,"UserNameError")

    def tearDown(self):
        self.db_connection.execute("DROP TABLE Users;")
        self.db_connection.execute("DROP TABLE Cost;")
        self.db_connection.execute("DROP TABLE Revenue;")
        self.db_connection.execute("DROP TABLE Plan;")
        self.db_connection.commit()
