from tkinter import ttk
from investment_plan_logic.plan_mgmt import get_costs, get_revenue

class InvestmentUi:
    def __init__(self,root,main_ui,plan_name):
        self._root = root
        self._main_ui = main_ui
        self.name = plan_name
        self._frame = None
        self._message_label = None
        self.initialise_view()
        self.load_plan()

    def initialise_view(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(index=0,pad=50, weight=1, minsize=500)
        self.show_message(f"Welcome to plan {self.name}. This view is a work in progress!")
        menu_button = ttk.Button(master=self._frame,text="Back to main menu",\
            command=self.handle_to_main_menu)
        menu_button.grid(padx=6, pady=4)

    def load_plan(self):
        costs = get_costs(self._main_ui.get_user(),self._main_ui.get_db(),self.name)
        revenue = get_revenue(self._main_ui.get_user(),self._main_ui.get_db(),self.name)

    def show_message(self,message):
        self._message_label = ttk.Label(master=self._frame, text = message)
        self._message_label.grid()

    def pack(self):
        self._frame.pack()

    def handle_to_main_menu(self):
        self._main_ui.show_menu_view()

    def destroy(self):
        self._frame.destroy()
