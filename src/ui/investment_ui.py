from tkinter import Tk,ttk, END
from investment_plan_logic.plan_mgmt import get_costs, get_revenue, add_cost, add_revenue, InputError

class InvestmentUi:
    def __init__(self,root,main_ui,plan_name):
        self._root = root
        self._main_ui = main_ui
        self.name = plan_name
        self._frame = None
        self._message_label = None
        self.costs = None
        self.revenue = None
        self.cost_popup = None
        self.revenue_popup = None
        self._cost_table = None
        self._revenue_table = None
        self.load_plan()
        self.initialise_view()

    def initialise_view(self):
        self._frame = ttk.Frame(master=self._root)
        #self._frame.grid_columnconfigure(index=0,pad=10, minsize=50)
        self.show_message(f"Welcome to plan {self.name}. This view is a work in progress!")      
        add_cost_button = menu_button = ttk.Button(master=self._frame,text="Add costs",\
            command=self.handle_add_cost)
        add_cost_button.grid(padx=20, pady=4, column=0, row=2)
        add_income_button = menu_button = ttk.Button(master=self._frame,text="Add income",\
            command=self.handle_add_revenue)
        add_income_button.grid(padx=20, pady=4, column=0, row=1)
        menu_button = ttk.Button(master=self._frame,text="Back to main menu",\
            command=self.handle_to_main_menu)
        menu_button.grid(padx=20, pady=4, column=0, row=0)
        graph_label = ttk.Label(master=self._frame, text="Graph will be here once I figure out matplotlib with poetry.")
        graph_label.grid(column=3, row=3)
        self.update_cost_table()
        self.update_revenue_table()
    
    def update_cost_table(self):
        cols = ('Description','Amount','Year')
        self._cost_table = ttk.Treeview(master=self._frame, columns=cols, show='headings')
        for col in cols:
            self._cost_table.column(col,width=100)
            self._cost_table.heading(col,text=col)
        total = 0
        for item in self.costs:
            self._cost_table.insert("", "end", values=(item[0],item[1],item[2]))
            total += item[1]
        self._cost_table.insert("","end", values=("total",total, "-"))
        self._cost_table.grid(row=3,column=1)

    def update_revenue_table(self):
        cols = ('Description','Amount','Year')
        self._revenue_table = ttk.Treeview(master=self._frame, columns=cols, show='headings')
        total = 0
        for col in cols:
            self._revenue_table.column(col,width=100)
            self._revenue_table.heading(col,text=col)
        for item in self.revenue:
            self._revenue_table.insert("", "end", values=(item[0],item[1],item[2]))
            total += item[1]
        self._revenue_table.insert("","end", values=("total",total, "-"))
        self._revenue_table.grid(row=4,column=1)

    def load_plan(self):
        self.costs = get_costs(self._main_ui.session.get_username(),
            self._main_ui.session.get_db_connection(),self.name)
        self.revenue = get_revenue(self._main_ui.session.get_username(),
            self._main_ui.session.get_db_connection(),self.name)

    def show_message(self,message):
        self._message_label = ttk.Label(master=self._frame, text = message)
        self._message_label.grid(row=0,column=1)

    def pack(self):
        self._frame.pack()

    def handle_to_main_menu(self):
        self._main_ui.show_menu_view()

    def handle_add_cost(self):
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
        while i < len(self.costs)+1:
            for j in range(3):
                entry = ttk.Entry(self.cost_popup, width=20)
                entry.insert(END,str(self.costs[i-1][j]))
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
        self.cost_popup.destroy()
        self.load_plan()
        self.update_cost_table()

    def exit_revenue_popup(self):
        self.revenue_popup.destroy()
        self.load_plan()
        self.update_revenue_table()

    def handle_add_revenue(self):
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
        while i < len(self.revenue):
            for j in range(3):
                entry = ttk.Entry(self.revenue_popup, width=20)
                entry.insert(END,str(self.revenue[i][j]))
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
        index = self.cost_popup.grid_size()[1]-3
        desc = self.cost_popup.grid_slaves(row=index,column=0)[0].get()
        amount = self.cost_popup.grid_slaves(row=index,column=1)[0].get()
        year = self.cost_popup.grid_slaves(row=index,column=2)[0].get()
        try:
            add_cost(self._main_ui.session.get_username(), self._main_ui.session.get_db_connection(),\
                self.name,desc,amount,year)
        except InputError as e:
            print(e)
        self.load_plan()
        self.cost_popup.destroy()
        self.handle_add_cost()

    def handle_add_revenueline(self):
        """Adds one more line to db"""
        index = self.revenue_popup.grid_size()[1]-3
        desc = self.revenue_popup.grid_slaves(row=index,column=0)[0].get()
        amount = self.revenue_popup.grid_slaves(row=index,column=1)[0].get()
        year = self.revenue_popup.grid_slaves(row=index,column=2)[0].get()
        try:
            add_revenue(self._main_ui.session.get_username(), self._main_ui.session.get_db_connection(),\
                self.name,desc,amount,year)
        except InputError as e:
            print(e)
        self.load_plan()
        self.revenue_popup.destroy()
        self.handle_add_revenue()

    def destroy(self):
        self._frame.destroy()
