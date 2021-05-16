class YearlyCosts:
    """Class used to hold list of costs for a particular year. Used by InvestmentPlan class
    """
    def __init__(self, cost):
        """constructor for yearly costs

        Args:
            cost (tuple): description, value, year
        """
        self.year = cost[2]
        self.costs = list()
        self.cost_sum = 0.0
        self.add_cost(cost)

    def add_cost(self, cost):
        """add a new cost item to the object

        Args:
            cost (tuple): description, value, year
        """
        self.costs.append((cost[0], cost[1], cost[2]))
        self.cost_sum += float(cost[1])

    def remove_cost(self, cost):
        self.costs.remove(cost[0],cost[1], cost[2])

    def get_costs(self):
        """used to get list of costs

        Returns:
            list of tuples: returns all cost items
             for the year in list (description, value, year)
        """
        return self.costs

    def get_cost_sum(self):
        """used to get the sum of all costs for the year

        Returns:
            float: sum of costs
        """
        return self.cost_sum
