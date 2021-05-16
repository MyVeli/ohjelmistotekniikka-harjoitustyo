import unittest
from db_mgmt import create_db
from logic.session_info import SessionInfo
from data_service.plan_service import create_plan
from logic.investment_plan import InvestmentPlan

class TestPlanMgmt(unittest.TestCase):
    def setUp(self):        
        self.db_name = ":memory:"
        self.db_connection = create_db(self.db_name)
        self.password = "testuser_pw"
        self.user = "testuser"
        self.session = SessionInfo()
        self.session.set_db_connection(self.db_connection)
        self.session.register(self.user, self.password)
        create_plan(self.user,self.db_connection,"test plan","description")
        self.plan = InvestmentPlan("test plan", self.session)
        self.plan.load_plan()
        self.plan.add_cost_item("cost", "500", "2020")
        self.plan.add_revenue_item("revenue", "500", "2020")
        self.plan.load_plan()

    def test_load_plan(self):
        test_plan = InvestmentPlan("test plan", self.session)
        test_plan.load_plan()
        self.assertEqual(len(test_plan.profits), len(self.plan.profits))

    def test_get_yearly_profit(self):
        self.assertEqual(0, self.plan.get_yearly_profit()[0][1])

    def test_get_yearly_costs(self):
        self.assertEqual(500, self.plan.get_yearly_costs()[0][1])

    def test_get_yearly_revenue(self):
        self.assertEqual(500, self.plan.get_yearly_revenue()[0][1])

    def test_get_costs(self):
        self.plan.add_cost_item("cost", "500", "2021")
        self.assertEqual(2, len(self.plan.get_costs()))

    def test_get_revenue(self):
        self.plan.add_revenue_item("rev", "500", "2021")
        self.assertEqual(2, len(self.plan.get_revenue()))

    def tearDown(self):
        self.db_connection.execute("DROP TABLE Users;")
        self.db_connection.execute("DROP TABLE Cost;")
        self.db_connection.execute("DROP TABLE Revenue;")
        self.db_connection.execute("DROP TABLE Plan;")
        self.db_connection.commit()
