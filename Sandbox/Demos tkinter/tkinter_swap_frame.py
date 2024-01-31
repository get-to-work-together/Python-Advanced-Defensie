import tkinter

import customtkinter as ctk


class Frame1(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0 , weight=1)

        w = ctk.CTkLabel(self, text='Frame 1', font=('Arial', 32), padx=100, pady=100)
        w.grid(row=0, column=0, sticky='we')

        w = ctk.CTkButton(self, text='to Frame 2', command=self.master.show_frame2)
        w.grid(row=1, column=0, pady=10)


class Frame2(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1)

        w = ctk.CTkLabel(self, text='Frame 2', font=('Arial', 32), padx=100, pady=100)
        w.grid(row=0, column=0, sticky='we')

        w = ctk.CTkButton(self, text='to Frame 1', command=self.master.show_frame1)
        w.grid(row=1, column=0, pady=10)


class App(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame1 = Frame1(self)
        self.frame1.grid(row=0, column=0, sticky='nsew')

        self.frame2 = Frame2(self)
        self.frame2.grid(row=0, column=0, sticky='nsew')

        self.show_frame1()

    def show_frame1(self):
        self.frame1.tkraise()

    def show_frame2(self):
        self.frame2.tkraise()



ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()

root.title("Demo tkinter Swap Frames")
root.geometry("500x300")

app = App(root)
app.pack(fill=ctk.BOTH, expand=True)

root.mainloop()
