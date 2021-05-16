import unittest
from logic.session_info import SessionInfo
from db_mgmt import create_db

class TestSessionInfo(unittest.TestCase):
    def setUp(self):        
        self.db_name = ":memory:"
        self.db_connection = create_db(self.db_name)
        self.password = "testuser_pw"
        self.user = "testuser"
        self.session = SessionInfo()
        self.session.set_db_connection(self.db_connection)

    def test_db_connection(self):
        self.assertEqual(self.db_connection, self.session.get_db_connection())

    def test_user_register(self):
        self.session.register(self.user, self.password)
        self.assertEqual(self.user, self.session.get_username())

    def test_login_user(self):
        self.session.__username__ = None
        try:
            self.session.register(self.user, self.password)
        except Exception as e:
            pass
        self.session.login(self.user, self.password)
        self.assertEqual(self.user, self.session.get_username())

    def tearDown(self):
        self.db_connection.execute("DROP TABLE Users;")
        self.db_connection.execute("DROP TABLE Cost;")
        self.db_connection.execute("DROP TABLE Revenue;")
        self.db_connection.execute("DROP TABLE Plan;")
        self.db_connection.commit()
