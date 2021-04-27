"""Main program which creates a db and starts UI."""
from tkinter import Tk
import db_mgmt
from ui.ui import UI

def main():
    """First creates db or gets db connection, then starts UI."""
    dbname = "investmentdb.db"
    db_connection = db_mgmt.create_db(dbname)
    window = Tk()
    window.title("Veli's investment program")
    ui_window = UI(window,db_connection)
    ui_window.start()
    window.mainloop()

main()
