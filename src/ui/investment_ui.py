"""Holds InvestmentUi class, which is used for the main view of the system.
"""
from tkinter import Tk,ttk, END
import matplotlib.pyplot as pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data_service.plan_service import InputError
from logic.investment_plan import InvestmentPlan

class InvestmentUi:
    """Class for managing the main UI of the system, which is for investment plan management.
    Requires root, main UI and plan name as parameters for init.
    """
    def __init__(self,root,main_ui,plan_name):
        self._root = root
        self._main_ui = main_ui
        self.name = plan_name
        self._frame = None
        self._message_label = None
        self.cost_popup = None
        self.revenue_popup = None
        self._cost_table = None
        self._revenue_table = None
        self.investment_plan = InvestmentPlan(plan_name, self._main_ui.session)
        self.investment_plan.load_plan()
        self.initialise_view()

    def initialise_view(self):
        """Initialises the view. Used by class constructor.
        """
        self._frame = ttk.Frame(master=self._root)
        self.show_message(f"You are editing plan {self.name}.")      
        add_cost_button = menu_button = ttk.Button(master=self._frame,text="Add costs",\
            command=self.handle_add_cost)
        add_cost_button.grid(padx=20, pady=4, column=0, row=2)
        add_income_button = menu_button = ttk.Button(master=self._frame,text="Add income",\
            command=self.handle_add_revenue)
        add_income_button.grid(padx=20, pady=4, column=0, row=3)
        menu_button = ttk.Button(master=self._frame,text="Back to main menu",\
            command=self.handle_to_main_menu)
        menu_button.grid(padx=20, pady=4, column=0, row=4)
        self.update_cost_table()
        self.update_revenue_table()
        self.draw_graph()
    
    def update_cost_table(self):
        """updates the values in the cost table.
        """
        table_label = ttk.Label(master=self._frame, text="costs")
        table_label.grid(row=1, column=2)
        cols = ('Description','Amount','Year')
        self._cost_table = ttk.Treeview(master=self._frame, columns=cols, show='headings')
        for col in cols:
            self._cost_table.column(col,width=100)
            self._cost_table.heading(col,text=col)
        total = 0
        for item in self.investment_plan.get_costs():
            self._cost_table.insert("", "end", values=(item[0],item[1],item[2]))
            total += item[1]
        self._cost_table.insert("","end", values=("total",total, "-"))
        self._cost_table.grid(row=2,column=1,rowspan=4,columnspan=4)

    def update_revenue_table(self):
        """Updates the values on the revenue table
        """
        table_label = ttk.Label(master=self._frame, text="revenue")
        table_label.grid(row=1, column=7)
        cols = ('Description','Amount','Year')
        self._revenue_table = ttk.Treeview(master=self._frame, columns=cols, show='headings')
        total = 0
        for col in cols:
            self._revenue_table.column(col,width=100)
            self._revenue_table.heading(col,text=col)
        for item in self.investment_plan.get_revenue():
            self._revenue_table.insert("", "end", values=(item[0],item[1],item[2]))
            total += item[1]
        self._revenue_table.insert("","end", values=("total",total, "-"))
        self._revenue_table.grid(row=2,column=6,rowspan=4,columnspan=4)

    def show_message(self,message):
        """Shows a message on the top of the main view.

        Args:
            message (string): message string to be shown.
        """
        self._message_label = ttk.Label(master=self._frame, text = message)
        self._message_label.grid(row=0,column=1, columnspan=6)

    def pack(self):
        self._frame.pack()

    def handle_to_main_menu(self):
        """Changes UI back to main menu.
        """
        self._main_ui.show_menu_view()

    def draw_graph(self):
        graph = pyplot.Figure(figsize=(6,5), dpi=100)
        draw_costs = list()
        draw_cost_years = list()
        for cost in self.investment_plan.get_yearly_costs():
            draw_costs.append(cost[1])
            draw_cost_years.append(cost[0])
        draw_rev = list()
        draw_rev_years = list()
        for rev in self.investment_plan.get_yearly_revenue():
            draw_rev.append(rev[1])
            draw_rev_years.append(rev[0])
        draw_profit = list()
        draw_profit_years = list()
        for profit in self.investment_plan.get_yearly_profit():
            draw_profit.append(profit[1])
            draw_profit_years.append(profit[0])
        graph.add_subplot(111).plot(draw_profit_years, draw_profit,\
            draw_cost_years, draw_costs, draw_rev_years, draw_rev)
        graph.legend(["profit", "costs", "revenue"])
        chart = FigureCanvasTkAgg(graph, self._frame)
        chart.get_tk_widget().grid(column = 1, row = 8, columnspan = 8, rowspan = 6)

    def handle_add_cost(self):
        """Creates a popup for adding new costs.
        """
        self.cost_popup = Tk()
        self.cost_popup.title("Costs")
        i = 0
        label = ttk.Label(self.cost_popup, width=20, text="Description")
        label.grid(row=i, column=0)
        label = ttk.Label(self.cost_popup, width=20, text="Amount")
        label.grid(row=i, column=1)
        label = ttk.Label(self.cost_popup, width=20, text="Year")
        label.grid(row=i, column=2)
        i += 1
        costs = self.investment_plan.get_costs()
        while i < len(costs) + 1:
            for j in range(3):
                entry = ttk.Entry(self.cost_popup, width=20)
                entry.insert(END,str(costs[i-1][j]))
                entry.grid(row=i, column=j)
            i += 1
        label = ttk.Label(master=self.cost_popup, text="Add new cost line:")
        label.grid(row = i)
        i += 1
        label = ttk.Label(self.cost_popup, width=20, text="Description")
        label.grid(row=i, column=0)
        label = ttk.Label(self.cost_popup, width=20, text="Amount")
        label.grid(row=i, column=1)
        label = ttk.Label(self.cost_popup, width=20, text="Year")
        label.grid(row=i, column=2)
        i += 1
        for j in range(3):
            entry = ttk.Entry(self.cost_popup, width=20)
            entry.grid(row=i, column=j)
        
        add_button = ttk.Button(self.cost_popup, text="Add line", command=self.handle_add_costline)
        add_button.grid(padx=6, pady=4)

        exit_button = ttk.Button(self.cost_popup, text="Back", command=self.exit_cost_popup)
        exit_button.grid(padx=6, pady=4)
        self.cost_popup.mainloop()

    def exit_cost_popup(self):
        """used for exiting cost popup and loading new costs to main view.
        """
        self.cost_popup.destroy()
        self.investment_plan.load_plan()
        self.update_cost_table()
        self.draw_graph()

    def exit_revenue_popup(self):
        """Used for exiting revenue popup and loads new revenue to main view.
        """
        self.revenue_popup.destroy()
        self.investment_plan.load_plan()
        self.update_revenue_table()
        self.draw_graph()

    def handle_add_revenue(self):
        """Creates a popup for adding new revenue items to the plan.
        """
        self.revenue_popup = Tk()
        self.revenue_popup.title("Revenue sources")
        i = 0
        label = ttk.Label(self.revenue_popup, width=20, text="Description")
        label.grid(row=i, column=0)
        label = ttk.Label(self.revenue_popup, width=20, text="Amount")
        label.grid(row=i, column=1)
        label = ttk.Label(self.revenue_popup, width=20, text="Year")
        label.grid(row=i, column=2)
        i += 1
        revenue = self.investment_plan.get_revenue()
        while i < len(revenue)+1:
            for j in range(3):
                entry = ttk.Entry(self.revenue_popup, width=20)
                entry.insert(END,str(revenue[i-1][j]))
                entry.grid(row=i, column=j)
            i += 1
        label = ttk.Label(master=self.revenue_popup, text="Add new revenue line:")
        label.grid(row = i)
        i += 1
        label = ttk.Label(self.revenue_popup, width=20, text="Description")
        label.grid(row=i, column=0)
        label = ttk.Label(self.revenue_popup, width=20, text="Amount")
        label.grid(row=i, column=1)
        label = ttk.Label(self.revenue_popup, width=20, text="Year")
        label.grid(row=i, column=2)
        i += 1
        for j in range(3):
            entry = ttk.Entry(self.revenue_popup, width=20)
            entry.grid(row=i, column=j)
        
        add_button = ttk.Button(self.revenue_popup, text="Add line", command=self.handle_add_revenueline)
        add_button.grid(padx=6, pady=4)

        exit_button = ttk.Button(self.revenue_popup, text="Back", command=self.exit_revenue_popup)
        exit_button.grid(padx=6, pady=4)
        self.revenue_popup.mainloop()

    def handle_add_costline(self):
        """Used for adding a single cost item to DB. Takes the values from the popup's grid
        """
        index = self.cost_popup.grid_size()[1]-3
        desc = self.cost_popup.grid_slaves(row=index,column=0)[0].get()
        amount = self.cost_popup.grid_slaves(row=index,column=1)[0].get()
        year = self.cost_popup.grid_slaves(row=index,column=2)[0].get()
        try:
            self.investment_plan.add_cost_item(desc, amount, year)
            self.investment_plan.load_plan()
        except InputError as _e:
            print(_e)
        self.cost_popup.destroy()
        self.handle_add_cost()

    def handle_add_revenueline(self):
        """Used for adding a single revenue item to DB. Takes the values from the popup's grid"""
        index = self.revenue_popup.grid_size()[1]-3
        desc = self.revenue_popup.grid_slaves(row=index,column=0)[0].get()
        amount = self.revenue_popup.grid_slaves(row=index,column=1)[0].get()
        year = self.revenue_popup.grid_slaves(row=index,column=2)[0].get()
        try:
            self.investment_plan.add_revenue_item(desc, amount, year)
            self.investment_plan.load_plan()
        except InputError as _e:
            print(_e)
        self.revenue_popup.destroy()
        self.handle_add_revenue()

    def destroy(self):
        """destroys the frame holding this UI
        """
        self._frame.destroy()
