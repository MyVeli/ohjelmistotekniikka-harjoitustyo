from tkinter import Tk, ttk
from ui.login_ui import LoginUi as login_ui
from ui.menu_ui import MainMenu

class UI:
    def __init__(self,root):
        self._root = root
        self._current_view = None
        self.user = None

    def start(self):
        self.show_login_view()

    def show_login_view(self):
        self.destroy_view()
        self._current_view = login_ui(self._root, self.menu)
        self._current_view.pack()

    def destroy_view(self):
        if self._current_view is not None:
            self._current_view.destroy()
        self._current_view = None
    
    def menu(self,username):
        self.destroy_view()
        self.user=username
        self._current_view = MainMenu(self._root, username, self.menu)
        self._current_view.pack()

if __name__ == "__main__":
    window = Tk()
    window.title("Welcome")
    ui = UI(window)
    ui.start()
    window.mainloop()
