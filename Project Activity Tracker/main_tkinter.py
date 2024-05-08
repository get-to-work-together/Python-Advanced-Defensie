import tkinter as tk
from src.gui.activity_input import App

root = tk.Tk()

# root.geometry('400x600+100+100')  # width x height + x_offset + y_offset
root.title('Activity Tracker Input')

app = App(root)

root.mainloop()