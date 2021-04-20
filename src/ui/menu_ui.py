from tkinter import ttk

class MainMenu:
    def __init__(self,root,user,next_ui):
        self._root = root
        self.next_ui = next_ui
        self._frame = None
        self.user = user
        self._message_label = None
        self.initialise_view()

    def initialise_view(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(index=0,pad=50, weight=1, minsize=500)
        self.show_message(f"Welcome {self.user}. There is still some work to be done!")

    def show_message(self,message):        
        self._message_label = ttk.Label(master=self._frame, text = message)
        self._message_label.grid()
    
    def pack(self):
        self._frame.pack()
