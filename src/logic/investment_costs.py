class YearlyCosts:
    """Class used to hold list of costs for a particular year. Used by InvestmentPlan class
    """
    def __init__(self, cost):
        self.year = cost[2]
        self.costs = list()
        self.cost_sum = 0.0
        self.add_cost(cost)

    def add_cost(self, cost):
        self.costs.append((cost[0], cost[1], cost[2]))
        self.cost_sum += float(cost[1])

    def remove_cost(self, cost):
        self.costs.remove(cost[0],cost[1], cost[2])

    def get_costs(self):
        return self.costs

    def get_cost_sum(self):
        return self.cost_sum
