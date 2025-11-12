import tkinter as tk
from tkinter import messagebox

top = tk.Tk()

def hello():
     messagebox.showinfo("Say Hello", "Hello World")

btn1 = tk.Button(top, text = "Say Hello", command = hello)
btn1.pack()

top.geometry('200x200')
top.mainloop()
