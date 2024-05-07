import tkinter as tk
from tkinter import tkMessageBox

top = tk.Tk()

def hello():
     tkMessageBox.showinfo("Say Hello", "Hello World")
btn1 = tk.Button(top, text = "Say Hello", command = hello)
btn1.pack()
top.mainloop()
