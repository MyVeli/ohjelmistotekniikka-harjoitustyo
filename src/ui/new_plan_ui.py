from tkinter import ttk
from logic.plan_mgmt import new_plan
from data_service.plan_service import InputError

class NewPlan:
    """UI for creating a new plan to the system.
    """
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
        """Used by constructor to initialise view.
        """
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(index=0,pad=50, weight=1, minsize=500)
        self.show_message("Welcome. Please create a plan by filling the required information below.")
        self._name_label = ttk.Label(master=self._frame, text = "Plan name: ")
        self._name_entry = ttk.Entry(master=self._frame)
        self._name_label.grid(padx=5, pady=5)
        self._name_entry.grid(padx=5, pady=5)

        self._description_label = ttk.Label(master=self._frame, text = "Plan description: ")
        self._description_entry = ttk.Entry(master=self._frame)
        self._description_label.grid(padx=5, pady=5)
        self._description_entry.grid(padx=40, pady=10)

        add_plan_button = ttk.Button(master=self._frame,text="Create",command=self._handle_new_plan)
        add_plan_button.grid(padx=6, pady=4)

        menu_button = ttk.Button(master=self._frame,text="Back",command=self._main_ui.show_menu_view)
        menu_button.grid(padx=6, pady=4)

    def show_message(self,message):
        """Shows a message in the view

        Args:
            message (string): message to show
        """
        self._message_label = ttk.Label(master=self._frame, text = message)
        self._message_label.grid()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack()

    def _handle_new_plan(self):
        try:
            new_plan(self._main_ui.session, self._name_entry.get(),\
            self._description_entry.get())
        except InputError as _e:
            self.show_message(str(_e))
        else:
            self._main_ui.show_investment_view(self._name_entry.get())
