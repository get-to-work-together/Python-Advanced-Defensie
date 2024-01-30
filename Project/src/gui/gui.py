# import tkinter as tk
import customtkinter as ctk

class ListFrame(ctk.CTkFrame):

    def __init__(self, master=None):
        super().__init__(master)


class DetailFrame(ctk.CTkFrame):

    def __init__(self, master=None):
        super().__init__(master)


class App(ctk.CTkFrame):

    def __init__(self, master=None):
        super().__init__(master)

        self.detail = DetailFrame(self)
        self.detail.grid(column=0, row=0, sticky='news')

        self.list = ListFrame(self)
        self.list.grid(column=0, row=0, sticky='news')

        self.show_list()

    def show_detail(self):
        self.detail.tkraise()

    def show_list(self):
        self.list.tkraise()







def main():
    root = ctk.CTk()
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('dark-blue')
    root.geometry('600x500+300+300')  # width x height + x_offset + y_offset
    root.resizable(width = False, height = False)
    root.title('My GUI')
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
