import tkinter as tk
import customtkinter as ctk

from Project.src.database.persistence import save_application_record

class ListFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        w = ctk.CTkLabel(self, text='Applicaties')
        w.grid(row=0, column=0, columnspan=2)

        applications = []
        self.applications = tk.Variable(value=applications)
        self.users_list = tk.Listbox(self, listvariable = self.applications)
        # self.update_list()
        self.users_list.grid(row=1, column=0, columnspan=2)

        kwargs = {'padx':20, 'pady':20}

        w = ctk.CTkButton(self, text='Toevoegen', command=self.handle_add)
        w.grid(row=2, column=0, **kwargs)

        w = ctk.CTkButton(self, text='Verwijderen', command=self.handle_remove)
        w.grid(row=2, column=1, **kwargs)

    def handle_add(self):
        self.master.show_detail()

    def handle_remove(self):
        pass
        # index = self.users_list.curselection()[0]
        # user_name = self.user_names.get()[index]
        # persistence = Persistence()
        # persistence.remove_user(user_name)
        # self.users_list.delete(index)

    def update_list(self):
        pass
        # persistence = Persistence()
        # user_names = persistence.get_user_names()
        # self.users_list.delete(0, tk.END)
        # self.users_list.insert(0, *user_names)


class DetailFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master

        kwargs = {'padx':20, 'pady':20}

        w = ctk.CTkLabel(self, text='Applicatie')
        w.grid(row=0, column=0, columnspan=2)

        w = ctk.CTkLabel(self, text='Name')
        w.grid(row=1, column=0, **kwargs)

        self.name = ctk.StringVar()

        w = ctk.CTkEntry(self, textvariable=self.name)
        w.grid(row=1, column=1, **kwargs)

        w = ctk.CTkLabel(self, text='Version')
        w.grid(row=2, column=0, **kwargs)

        self.version = ctk.StringVar()

        w = ctk.CTkEntry(self, textvariable=self.version)
        w.grid(row=2, column=1, **kwargs)

        w = ctk.CTkButton(self, text='Cancel', command=self.handle_cancel)
        w.grid(row=3, column=0, **kwargs)

        w = ctk.CTkButton(self, text='Save', command=self.handle_save)
        w.grid(row=3, column=1, **kwargs)

    def handle_cancel(self):
        self.master.show_list()

    def handle_save(self):
        save_application_record(self.name.get(), self.version.get())
        self.master.show_list()


class App(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.detail = DetailFrame(self)
        self.detail.grid(column=0, row=0, sticky='nwse')

        self.list = ListFrame(self)
        self.list.grid(column=0, row=0, sticky='nwse')

        self.show_detail()

    def show_detail(self):
        self.list.forget()
        self.detail.tkraise()

    def show_list(self):
        self.detail.forget()
        self.list.tkraise()







def main():
    root = ctk.CTk()
    # cctk.CTkset_appearance_mode('light')
    # cctk.CTkset_default_color_theme('dark-blue')
    root.geometry('600x500+300+300')  # width x height + x_offset + y_offset
    root.resizable(width = False, height = False)
    root.title('My GUI')
    app = App(root)
    app.pack(fill=ctk.BOTH, expand=True)
    root.mainloop()


if __name__ == '__main__':
    main()
