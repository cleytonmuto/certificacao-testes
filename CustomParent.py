import tkinter as tk
from tkinter import ttk
import CustomChild

class Parent(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.geometry('300x200')
        self.title('Main Window')

        # place a button on the root window
        ttk.Button(self, text='Open a window', command=self.open_window).pack(expand=True)

    def open_window(self):
        window = CustomChild.CustomChild(self)
        window.grab_set()

if __name__ == "__main__":
    app = Parent()
    app.mainloop()