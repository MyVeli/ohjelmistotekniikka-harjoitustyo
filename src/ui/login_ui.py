"""UI component used for registration and logging in."""
from tkinter import ttk
from user_mgmt.login import user_login as login, CredentialError
from user_mgmt.register import register_user as register, UserNameError, PasswordError

class LoginUi:
    def __init__(self,root,main_ui):
        self._root = root
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._username_label = None
        self._password_label = None
        self.message = None
        self._error_label = None
        self.main_ui = main_ui
        self.initialise_view()

    def initialise_view(self):
        self._frame = ttk.Frame(master=self._root)

        #username components:
        self._username_label = ttk.Label(master=self._frame, text = "Username: ")
        self._username_entry = ttk.Entry(master=self._frame)
        self._username_label.grid(padx=5, pady=5)
        self._username_entry.grid(padx=5, pady=5)

        #password components
        self._password_label = ttk.Label(master=self._frame, text = "Password: ")
        self._password_entry = ttk.Entry(master=self._frame)
        self._password_label.grid(padx=5, pady=5)
        self._password_entry.grid(padx=5, pady=5)

        login_button = ttk.Button(master=self._frame,text="Login",command=self.handle_login)
        register_button = ttk.Button(master=self._frame,text="Register",
                            command=self.handle_registration)
        login_button.grid(padx=6, pady=4)
        register_button.grid(padx=6, pady=4)
        self._frame.grid_columnconfigure(index=0,pad=50, weight=1, minsize=500)

    def destroy(self):
        self._frame.destroy()

    def show_error_message(self,error_message):
        self._error_label = ttk.Label(master=self._frame, text = error_message)
        self._error_label.grid()

    def handle_login(self):
        try:
            username = login(self._username_entry.get(),\
                self._password_entry.get(),"investmentdb.db")
            self.main_ui.set_user(username)
            self.main_ui.show_menu_view()
        except CredentialError:
            self.show_error_message("Wrong username or password.")
        except ConnectionError:
            self.show_error_message("Problem with DB connection.")

    def handle_registration(self):
        try:
            username = register(self._username_entry.get(),\
                self._password_entry.get(),"investmentdb.db")
            self.main_ui.set_user(username)
            self.main_ui.show_menu_view()
        except UserNameError:
            self.show_error_message("Username already in use")
        except PasswordError:
            self.show_error_message("Too short password. Use at least 5 characters.")
        except ConnectionError:
            self.show_error_message("Problem with DB connection.")

    def pack(self):
        self._frame.pack()
