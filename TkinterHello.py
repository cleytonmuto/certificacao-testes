import tkinter as tk

class TkinterHello:

    def __init__(self):
        pass

    def run(self):
        rootWidget = tk.Tk()
        labelWidget = tk.Label(rootWidget,text="\nHello, World!")
        labelWidget.config(font=("Arial",24))
        labelWidget.pack()
        rootWidget.mainloop()

test = TkinterHello()
test.run()
