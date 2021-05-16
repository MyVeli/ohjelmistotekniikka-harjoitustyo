from tkinter import ttk,Listbox,END,ACTIVE
from data_service.plan_service import InputError
from logic.plan_mgmt import load_plans

class MainMenu:
    """UI class used for showing the mainmenu, 
    letting the user select between adding and loading a plan.
    """
    def __init__(self,root,ui):
        """constructor

        Args:
            root (TK): UI root
            ui (UI): main UI class
        """
        self._root = root
        self._main_ui = ui
        self._frame = None
        self._message_label = None
        self.initialise_view()

    def initialise_view(self):
        """Used by constructor to initialise the view.
        """
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(index=0,pad=50, weight=1, minsize=500)
        self.show_message(f"Welcome {self._main_ui.session.get_username()}.")
        new_plan_button = ttk.Button(master=self._frame,text="New plan",
                            command=self.handle_new_plan)
        load_plan_button = ttk.Button(master=self._frame,text="Load plan",
                            command=self.handle_load_plan)
        new_plan_button.grid(padx=6, pady=4)
        load_plan_button.grid(padx=6, pady=4)

    def show_message(self,message):
        """Shows a message on the UI.

        Args:
            message (string): message to be shown.
        """
        self._message_label = ttk.Label(master=self._frame, text = message)
        self._message_label.grid()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def handle_load_plan(self):
        """shows the load plan view
        """
        self._main_ui.show_load_view()

    def handle_new_plan(self):
        """shows the add a new plan view.
        """
        self._main_ui.show_create_new_plan()


class LoadMenu:
    """UI class for the load a plan menu.
    """
    def __init__(self,root,ui):
        """constructor

        Args:
            root (TK): UI root
            ui (UI): main UI class
        """
        self._root = root
        self._main_ui = ui
        self._frame = None
        self._message_label = None
        self._list = None
        self.initialise_view()

    def initialise_view(self):
        """Used by the constructor to initialise the view.
        """
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(index=0,pad=50, weight=1, minsize=500)
        self._list = Listbox(self._frame)
        self.show_message("Welcome. Please choose a plan from the list")
        plans = self.get_plans()
        for i in plans:
            self._list.insert(END,i[0])
        self._list.grid()
        load_plan_button = ttk.Button(master=self._frame,text="Load plan",
                            command=self.handle_load_plan)
        load_plan_button.grid(padx=6, pady=4)

        menu_button = ttk.Button(master=self._frame,text="Back",command=self._main_ui.show_menu_view)
        menu_button.grid(padx=6, pady=4)

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def show_message(self,message):
        """Used for showing a message on the view.

        Args:
            message (string): message to be shown.
        """
        self._message_label = ttk.Label(master=self._frame, text = message)
        self._message_label.grid()

    def handle_load_plan(self):
        """Shows the investment view with the chosen plan.
        """
        if self._list.get(ACTIVE) is not None and len(self._list.get(ACTIVE)) > 0:
            self._main_ui.show_investment_view(self._list.get(ACTIVE))

    def get_plans(self):
        """returns all the plans for the user.

        Returns:
            list of strings: plan names in a list 
        """
        return load_plans(self._main_ui.session)
