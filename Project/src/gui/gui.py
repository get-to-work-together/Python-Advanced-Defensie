import tkinter as tk
import customtkinter as ctk


class ListFrame(tk.Frame):

    def __init__(self, master):
        super().__init__()

        w = tk.Label(master, text='LIST')
        w.grid(row=0, column=0)

        w = tk.Label(master, text='LIST1')
        w.grid(row=1, column=0)

        w = tk.Label(master, text='LIST2')
        w.grid(row=2, column=0)

        w = tk.Label(master, text='LIST3')
        w.grid(row=3, column=0)


class DetailFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        w = tk.Label(master, text='DETAIL')
        w.grid(row=0, column=0)
        # w.pack()


class App(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.detail = DetailFrame(self)
        self.detail.grid(column=0, row=0, sticky='news')
        # self.detail.grid()
        # self.detail.pack()

        self.list = ListFrame(self)
        self.list.grid(column=0, row=0, sticky='news')
        # self.list.grid()
        # self.list.pack()

        self.show_detail()

    def show_detail(self):
        self.detail.tkraise()

    def show_list(self):
        self.list.tkraise()







def main():
    root = tk.Tk()
    # ctk.set_appearance_mode('light')
    # ctk.set_default_color_theme('dark-blue')
    root.geometry('600x500+300+300')  # width x height + x_offset + y_offset
    root.resizable(width = False, height = False)
    root.title('My GUI')
    app = DetailFrame(root)
    app.grid(sticky='news')
    root.mainloop()


if __name__ == '__main__':
    main()
