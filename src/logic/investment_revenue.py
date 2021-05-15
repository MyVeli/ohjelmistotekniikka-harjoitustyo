class YearlyRevenue:
    """Class for holding revenue items for one year. Is used by InvestmentPlan class.
    """
    def __init__(self, rev):
        self.year = rev[2]
        self.revenue = list()
        self.rev_sum = 0
        self.add_revenue(rev)

    def add_revenue(self, rev):
        self.revenue.append((rev[0], rev[1], rev[2]))
        self.rev_sum += float(rev[1])

    def get_revenue(self):
        return self.revenue

    def get_revenue_sum(self):
        return self.rev_sum
