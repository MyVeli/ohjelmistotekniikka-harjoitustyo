import unittest
from logic.investment_revenue import YearlyRevenue

class TestRevenueMgmt(unittest.TestCase):
    def setUp(self):
        self.year = "2020"
        revenue_item = ("first_item", "500.0", self.year)        
        self.yearly_revenue_item = YearlyRevenue(revenue_item)

    def test_add_revenue_get_revenue(self):
        revenue_item = ("second_item", "500.0", self.year)
        self.yearly_revenue_item.add_revenue(revenue_item)
        self.assertEqual(len(self.yearly_revenue_item.get_revenue()),2)
        self.assertEqual(self.yearly_revenue_item.get_revenue()[1], revenue_item)

    def test_revenue_sum(self):
        revenue_item = ("second_item", "500.0", self.year)
        self.yearly_revenue_item.add_revenue(revenue_item)
        self.assertEqual(self.yearly_revenue_item.get_revenue_sum(), 1000)
