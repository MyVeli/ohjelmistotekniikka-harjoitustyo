from tkinter import ttk,Listbox,END
from investment_plan_logic.plan_mgmt import get_plans_by_user

class MainMenu:
    def __init__(self,root,user,ui):
        self._root = root
        self._main_ui = ui
        self._frame = None
        self.user = user
        self._message_label = None
        self.initialise_view()

    def initialise_view(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(index=0,pad=50, weight=1, minsize=500)
        self.show_message(f"Welcome {self.user}. There is still some work to be done!")
        new_plan_button = ttk.Button(master=self._frame,text="New plan",
                            command=self.handle_new_plan)
        load_plan_button = ttk.Button(master=self._frame,text="Load plan",
                            command=self.handle_load_plan)
        new_plan_button.grid(padx=6, pady=4)
        load_plan_button.grid(padx=6, pady=4)

    def show_message(self,message):
        self._message_label = ttk.Label(master=self._frame, text = message)
        self._message_label.grid()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def handle_load_plan(self):
        self._main_ui.show_load_view()

    def handle_new_plan(self):
        self._main_ui.show_create_new_plan()


class LoadMenu:
    def __init__(self,root,ui):
        self._root = root
        self._main_ui = ui
        self._frame = None
        self._message_label = None
        self._list = None
        self.initialise_view()

    def initialise_view(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(index=0,pad=50, weight=1, minsize=500)
        self._list = Listbox(self._frame)
        self.show_message("Welcome. There is still some work to be done!")
        plans = self.get_plans()
        for i in plans:
            self._list.insert(END,i[0])
        self._list.grid()
        load_plan_button = ttk.Button(master=self._frame,text="Load plan",
                            command=self.handle_load_plan)
        load_plan_button.grid(padx=6, pady=4)

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def show_message(self,message):
        self._message_label = ttk.Label(master=self._frame, text = message)
        self._message_label.grid()

    def handle_load_plan(self):
        self._main_ui.show_menu_view()

    def get_plans(self):
        return get_plans_by_user(self._main_ui.get_user(),self._main_ui.get_db())
