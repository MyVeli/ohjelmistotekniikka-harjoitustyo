"""Used for managing the UI in the system. Changes between different views and holds root.
"""
from ui.login_ui import LoginUi as login_ui
from ui.menu_ui import MainMenu, LoadMenu
from ui.new_plan_ui import NewPlan
from ui.investment_ui import InvestmentUi
from logic.session_info import SessionInfo

class UI:
    """Main UI class which holds the root and changes between Uis.
    """
    def __init__(self,root,db):
        """constructor for the main UI.

        Args:
            root (TK): Tk
            db (sqlite 3 connection): database connection
        """
        self._root = root
        self._current_view = None
        self.session = SessionInfo()
        self.session.set_db_connection(db)

    def start(self):
        """Start shows the login view.
        """
        self.show_login_view()

    def show_login_view(self):
        """Shows the login view.
        """
        self.destroy_view()
        self._current_view = login_ui(self._root, self)
        self._current_view.pack()

    def destroy_view(self):
        """Destroys current view
        """
        if self._current_view is not None:
            self._current_view.destroy()
        self._current_view = None

    def show_menu_view(self):
        """Shows the main menu view
        """
        self.destroy_view()
        self._current_view = MainMenu(self._root,self)
        self._current_view.pack()

    def show_load_view(self):
        """Shows the load investment plan view
        """
        self.destroy_view()
        self._current_view = LoadMenu(self._root,self)
        self._current_view.pack()

    def show_create_new_plan(self):
        """Shows the ui for creating a new plan.
        """
        self.destroy_view()
        self._current_view = NewPlan(self._root,self)
        self._current_view.pack()

    def show_investment_view(self,plan_name):
        """Shows the investment plan view.

        Args:
            plan_name (string): name of the plan to show.
        """
        self.destroy_view()
        self._current_view = InvestmentUi(self._root,self,plan_name)
        self._current_view.pack()
