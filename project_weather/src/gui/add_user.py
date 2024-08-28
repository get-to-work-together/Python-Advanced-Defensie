try:
    from ..models.database.db_sqlite import insert_user
    from ..models.database.user import User

except:
    import os
    project_path = '../..'
    os.chdir(project_path)
    from src.models.database.db_sqlite import insert_user
    from src.models.database.user import User


import tkinter as tk



class App(tk.Frame):

    def __init__(self, master=None):

        w = tk.Label(master, text='Username')
        w.grid(row=0, column=0, padx=6, pady=3)

        self.txt_username = tk.StringVar()
        w = tk.Entry(master, textvariable=self.txt_username)
        w.grid(row=0, column=1, padx=6, pady=3)

        w = tk.Label(master, text='Password')
        w.grid(row=1, column=0, padx=6, pady=3)

        self.txt_password = tk.StringVar()
        w = tk.Entry(master, textvariable=self.txt_password, show='*')
        w.grid(row=1, column=1, padx=6, pady=3)

        w = tk.Label(master, text='E-mail')
        w.grid(row=2, column=0, padx=6, pady=3)

        self.txt_email = tk.StringVar()
        w = tk.Entry(master, textvariable=self.txt_email)
        w.grid(row=2, column=1, padx=6, pady=3)

        btn = tk.Button(master, text='Add User', command=self.button_handler)
        btn.grid(row=3, column=0, columnspan=2, padx=6, pady=3)

    def button_handler(self):
        user = User(self.txt_username.get(), self.txt_password.get(), self.txt_email.get())
        insert_user(user)


def main():
    root = tk.Tk()

    root.geometry('300x200+100+100')  # width x height + x_offset + y_offset
    root.title('Add User')

    app = App(root)

    root.mainloop()


if __name__ == '__main__':

    main()