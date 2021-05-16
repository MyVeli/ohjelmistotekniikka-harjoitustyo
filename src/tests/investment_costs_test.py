import unittest
from logic.investment_costs import YearlyCosts

class TestYearlyCosts(unittest.TestCase):
    def setUp(self):
        self.year = "2020"
        cost_item = ("first_item", "500.0", self.year)        
        self.yearly_cost_item = YearlyCosts(cost_item)

    def test_add_cost_get_costs(self):
        cost_item = ("second_item", "500.0", self.year)
        self.yearly_cost_item.add_cost(cost_item)
        self.assertEqual(len(self.yearly_cost_item.get_costs()),2)
        self.assertEqual(self.yearly_cost_item.get_costs()[1], cost_item)

    def test_cost_sum(self):
        cost_item = ("second_item", "500.0", self.year)
        self.yearly_cost_item.add_cost(cost_item)
        self.assertEqual(self.yearly_cost_item.get_cost_sum(), 1000)
