import unittest
import sqlite3
from user_mgmt.register import register_user
from db_mgmt import create_db
from investment_plan_logic.plan_mgmt import create_plan

class TestPlanMgmt(unittest.TestCase):
    def setUp(self):        
        self.db_name = "plantest.db"
        self.db_connection = create_db(self.db_name)
        self.password = "testuser_pw"
        self.user = "testuser"
        register_user(self.user,self.password,self.db_name)

    def test_add_plan(self):
        create_plan(self.user,self.db_connection,"test plan","description")
        result = self.db_connection.execute("SELECT name, description FROM Plan").fetchone()
        self.assertEqual(result[0],"test plan")
        self.assertEqual(result[1], "description")

    def tearDown(self):
        self.db_connection.execute("DROP TABLE Users;")
        self.db_connection.execute("DROP TABLE Cost;")
        self.db_connection.execute("DROP TABLE Revenue;")
        self.db_connection.execute("DROP TABLE Plan;")
        self.db_connection.commit()