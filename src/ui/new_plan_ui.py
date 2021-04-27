from tkinter import ttk
from investment_plan_logic.plan_mgmt import create_plan

class NewPlan:
    def __init__(self,root,ui):
        self._root = root
        self._main_ui = ui
        self._frame = None
        self._name_label = None
        self._name_entry = None
        self._description_label = None
        self._message_label = None
        self._description_entry = None
        self.initialise_view()

    def initialise_view(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(index=0,pad=50, weight=1, minsize=500)
        self.show_message("Welcome. There is still some work to be done!")
        self._name_label = ttk.Label(master=self._frame, text = "Plan name: ")
        self._name_entry = ttk.Entry(master=self._frame)
        self._name_label.grid(padx=5, pady=5)
        self._name_entry.grid(padx=5, pady=5)

        self._description_label = ttk.Label(master=self._frame, text = "Plan description: ")
        self._description_entry = ttk.Entry(master=self._frame)
        self._description_label.grid(padx=5, pady=5)
        self._description_entry.grid(padx=40, pady=10)

        add_plan_button = ttk.Button(master=self._frame,text="Create",command=self.handle_new_plan)
        add_plan_button.grid(padx=6, pady=4)

    def show_message(self,message):
        self._message_label = ttk.Label(master=self._frame, text = message)
        self._message_label.grid()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack()

    def handle_new_plan(self):
        create_plan(self._main_ui.get_user(),self._main_ui.get_db(),\
            self._name_entry.get(),self._description_entry.get())
        self._main_ui.show_investment_view(self._name_entry.get())
