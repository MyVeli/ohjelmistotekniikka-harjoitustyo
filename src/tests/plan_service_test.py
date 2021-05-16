import unittest
from data_service.register import register_user
from db_mgmt import create_db
from data_service.plan_service import create_plan, get_plans_by_user, get_revenue, \
    get_costs, add_revenue, add_cost

class TestPlanMgmt(unittest.TestCase):
    def setUp(self):        
        self.db_name = ":memory:"
        self.db_connection = create_db(self.db_name)
        self.password = "testuser_pw"
        self.user = "testuser"
        register_user(self.user,self.password,self.db_connection)
        create_plan(self.user,self.db_connection,"test plan","description")

    def test_add_plan(self):
        result = self.db_connection.execute("SELECT name, description FROM Plan").fetchone()
        self.assertEqual(result[0],"test plan")
        self.assertEqual(result[1], "description")

    def test_get_plan(self):
        self.assertEqual(get_plans_by_user(self.user, self.db_connection)[0][0],"test plan")

    def test_add_cost_get_cost(self):
        add_cost(self.user, self.db_connection, "test plan", "cost", "50", "2020")
        cost = get_costs(self.user, self.db_connection, "test plan")
        self.assertEqual(cost[0][0],"cost")
        self.assertEqual(cost[0][1], 50)
        self.assertEqual(cost[0][2], 2020)

    def test_add_revenue_get_revenue(self):
        add_revenue(self.user, self.db_connection, "test plan", "rev", "50", "2020")
        rev = get_revenue(self.user, self.db_connection, "test plan")
        self.assertEqual(rev[0][0],"rev")
        self.assertEqual(rev[0][1], 50)
        self.assertEqual(rev[0][2], 2020)

    def tearDown(self):
        self.db_connection.execute("DROP TABLE Users;")
        self.db_connection.execute("DROP TABLE Cost;")
        self.db_connection.execute("DROP TABLE Revenue;")
        self.db_connection.execute("DROP TABLE Plan;")
        self.db_connection.commit()
