import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(filetypes = [('Python', '.py')])

print('Opening file ...', file_path)
