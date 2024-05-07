import tkinter as tk

class App(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.activity_name = tk.StringVar()
        tk.Label(master, text="Name:").grid(row=0, sticky=tk.W, padx=20)
        self.e1 = tk.Entry(master, textvariable=self.activity_name)
        self.e1.grid(row=0, column=1, padx=40)

        self.activity_type = tk.StringVar()
        tk.Label(master, text="Activity type:").grid(row=1, sticky=tk.W, padx=20)
        self.e2 = tk.Entry(master, textvariable=self.activity_type)
        self.e2.grid(row=1, column=1, padx=20)

        self.activity_date_due = tk.StringVar()
        tk.Label(master, text="Date due:").grid(row=2, sticky=tk.W, padx=20)
        self.e3 = tk.Entry(master, textvariable=self.activity_date_due)
        self.e3.grid(row=2, column=1, padx=20)

        self.activity_note = tk.StringVar()
        tk.Label(master, text="Note:").grid(row=3, sticky=tk.W, padx=20)
        self.e4 = tk.Entry(master, textvariable=self.activity_note)
        self.e4.grid(row=3, column=1, padx=20)

        self.activity_duration = tk.StringVar()
        tk.Label(master, text="Duration:").grid(row=4, sticky=tk.W, padx=20)
        self.e5 = tk.Entry(master, textvariable=self.activity_duration)
        self.e5.grid(row=4, column=1, padx=20)

        self.activity_object = tk.StringVar()
        tk.Label(master, text="Object:").grid(row=5, sticky=tk.W, padx=20)
        self.e6 = tk.Entry(master, textvariable=self.activity_object)
        self.e6.grid(row=5, column=1, padx=20)

        self.activity_assigned_to = tk.StringVar()
        tk.Label(master, text="Assigned to:").grid(row=6, sticky=tk.W, padx=20)
        self.e7 = tk.Entry(master, textvariable=self.activity_assigned_to)
        self.e7.grid(row=6, column=1, padx=20)

        self.activity_status = tk.StringVar()
        tk.Label(master, text="Status:").grid(row=7, sticky=tk.W, padx=20)
        self.e8 = tk.Entry(master, textvariable=self.activity_status)
        self.e8.grid(row=7, column=1, padx=20)

        self.button = tk.Button(master, text="Save")
        self.button.grid(row=8, columnspan=2, sticky=tk.EW)


if __name__ == '__main__':

    root = tk.Tk()

    root.geometry('400x600+100+100')  # width x height + x_offset + y_offset
    root.title('Activity Tracker Input')

    app = App(root)

    root.mainloop()
