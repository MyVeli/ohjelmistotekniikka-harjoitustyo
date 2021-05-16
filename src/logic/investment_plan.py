from data_service.plan_service import get_costs, get_revenue, add_cost, add_revenue, InputError
from logic.investment_costs import YearlyCosts
from logic.investment_revenue import YearlyRevenue

class InvestmentPlan:
    """Class for handling investment plans, including costs, revenue & profit.
    """
    def __init__(self, name, session):
        """Class constructor for investment plans. Needs InvestmentPlan.load_plan() afterwards.

        Args:
            name (string): name of the plan. Used to connect to the right plan in db
            session (logic.SessionInfo object): information for connecting and using the db
        """
        self.plan_name = name
        self.session = session
        self.costs = None
        self.revenue = None
        self.profits = None

    def load_plan(self):
        """Loads all values for the plan from the database with the plan name and session
        information given in constructor.
        """
        self.costs = dict()
        self.revenue = dict()
        self.profits = dict()
        costs = get_costs(self.session.get_username(),
            self.session.get_db_connection(),self.plan_name)
        revenue = get_revenue(self.session.get_username(),
            self.session.get_db_connection(),self.plan_name)

        for cost in costs:
            if cost[2] in self.costs:
                self.costs[cost[2]].add_cost(cost)
            else:
                self.costs[cost[2]] = YearlyCosts(cost)
            if cost[2] in self.profits:
                self.profits[cost[2]] -= float(cost[1])
            else:
                self.profits[cost[2]] = -float(cost[1])
        for rev in revenue:
            if rev[2] in self.revenue:
                self.revenue[rev[2]].add_revenue(rev)
            else:
                self.revenue[rev[2]] = YearlyRevenue(rev)
            if rev[2] in self.profits:
                self.profits[rev[2]] += float(rev[1])
            else:
                self.profits[rev[2]] = float(rev[1])

    def get_yearly_profit(self):
        """Get yearly profits for the plan.

        Returns:
            (list of tuples): list of tuples with year and the year's total profit.
        """
        result = list()
        for year, profit in self.profits.items():
            result.append((year, profit))
        result.sort()
        return result

    def get_yearly_costs(self):
        """Get yearly costs for the plan.

        Returns:
            (list of tuples): list of tuples with year and the year's total costs
        """
        result = list()
        for year, value in self.costs.items():
            result.append((year, value.get_cost_sum()))
        result.sort()
        return result

    def get_yearly_revenue(self):
        """Get yearly revenue for the plan

        Returns:
            (list of tuples): list of tuples with year and the year's total revenue
        """
        result = list()
        for year, value in self.revenue.items():
            result.append((year, value.get_revenue_sum()))
        result.sort()
        return result

    def get_costs(self):
        """Get all costs for the plan

        Returns:
            (list of tuples): list of tuples with cost description, amount and year
        """
        result = list()
        for cost in self.costs.values():
            result.extend(cost.get_costs())
        return result

    def get_revenue(self):
        """Get all revenue items for the plan

        Returns:
            (list of tuples): list of tuples with revenue description, amount and year
        """
        result = list()
        for rev in self.revenue.values():
            result.extend(rev.get_revenue())
        return result

    def add_cost_item(self, desc, amount, year):
        """Adds a cost item to the DB & this object

        Args:
            desc (string): description or name of cost
            amount (string, int or float): amount of money
            year (string or int): year for the cost
        """
        try:
            self._verify_input(desc, amount, year)
        except InputError as _e:
            raise _e
        add_cost(self.session.get_username(), self.session.get_db_connection(),\
                self.plan_name, desc, amount, year)
        if year in self.costs:
            self.costs[year].add_cost((desc, amount, year))
        else:
            self.costs[year] = YearlyCosts((desc, amount, year))

    def add_revenue_item(self, desc, amount, year):
        """Adds a revenue item to the DB & this object

        Args:
            desc (string): description of the revenue item
            amount (string, int or float): amount of money
            year (string or int): year for the revenue
        """
        try:
            self._verify_input(desc, amount, year)
        except InputError as _e:
            raise _e
        add_revenue(self.session.get_username(), self.session.get_db_connection(),\
                self.plan_name, desc, amount, year)
        if year in self.revenue:
            self.revenue[year].add_revenue((desc, amount, year))
        else:
            self.revenue[year] = YearlyRevenue((desc, amount, year))

    def _verify_input(self, desc, amount, year):
        if desc is None or len(desc) < 1 or len(desc) > 25:
            raise InputError("Please keep description between 1 and 25 characters.")
        try:
            amount = float(amount)
            year = float(year)
        except ValueError:
            raise InputError("Please give year and amount as number")
        if year < 0 or amount < 0:
            raise InputError("Please only use positive numbers with amount and year")
