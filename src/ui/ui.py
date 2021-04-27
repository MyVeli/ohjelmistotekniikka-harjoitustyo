from ui.login_ui import LoginUi as login_ui
from ui.menu_ui import MainMenu, LoadMenu
from ui.new_plan_ui import NewPlan
from ui.investment_ui import InvestmentUi

class UI:
    def __init__(self,root,db):
        self._root = root
        self._current_view = None
        self.__user__ = None
        self.__db__ = db

    def get_user(self):
        return self.__user__

    def set_user(self,username):
        self.__user__ = username

    def get_db(self):
        return self.__db__

    def start(self):
        self.show_login_view()

    def show_login_view(self):
        self.destroy_view()
        self._current_view = login_ui(self._root, self)
        self._current_view.pack()

    def destroy_view(self):
        if self._current_view is not None:
            self._current_view.destroy()
        self._current_view = None

    def show_menu_view(self):
        self.destroy_view()
        self._current_view = MainMenu(self._root, self.__user__,self)
        self._current_view.pack()

    def show_load_view(self):
        self.destroy_view()
        self._current_view = LoadMenu(self._root,self)
        self._current_view.pack()

    def show_create_new_plan(self):
        self.destroy_view()
        self._current_view = NewPlan(self._root,self)
        self._current_view.pack()

    def show_investment_view(self,plan_name):
        self.destroy_view()
        self._current_view = InvestmentUi(self._root,self,plan_name)
        self._current_view.pack()
