import tkinter as tk
import customtkinter as ctk

from Project.src.database.persistence import save_application_record

class ListFrame(tk.Frame):

    def __init__(self, master):
        super().__init__()

        self.master = master

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

        self.master = master

        w = tk.Label(master, text='Name')
        w.grid(row=0, column=0)

        self.name = tk.StringVar()

        w = tk.Entry(master, textvariable=self.name)
        w.grid(row=0, column=1)

        w = tk.Label(master, text='Version')
        w.grid(row=1, column=0)

        self.version = tk.StringVar()

        w = tk.Entry(master, textvariable=self.version)
        w.grid(row=1, column=1)

        w = tk.Button(master, text='Cancel', command=self.handle_cancel)
        w.grid(row=2, column=0)

        w = tk.Button(master, text='Save', command=self.handle_save)
        w.grid(row=2, column=1)

    def handle_cancel(self):
        print('cancel')

    def handle_save(self):
        save_application_record(self.name.get(), self.version.get())
        print('save', self.name.get(), self.version.get())


class App(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.detail = DetailFrame(self)
        self.detail.grid(column=0, row=0, sticky='news')

        self.list = ListFrame(self)
        self.list.grid(column=0, row=0, sticky='news')

        self.show_detail()

    def show_detail(self):
        self.list.forget()
        self.detail.tkraise()

    def show_list(self):
        self.detail.forget()
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
