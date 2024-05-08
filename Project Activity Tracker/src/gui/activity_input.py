import sys
import tkinter as tk
from datetime import date, datetime

try:
    from ..models.activity import Activity
    from ..repository.repository import ActivityRepository
    from ..data_store.as_sqlite import store_activity
except:
    sys.path.append(r'/Users/peter/Computrain/_InCompany/Defensie/Python Advanced/Project Activity Tracker/src')
    from models.activity import Activity
    from repository.repository import ActivityRepository
    from data_store.as_sqlite import store_activity

activity_types = ['routine onderhoud', 'incident', 'uitgeleend retour']
status_values = sorted(['open','gedaan','geannuleerd','mislukt','in progress','vertraagd'])

class App(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        row = 0
        tk.Label(master, text="Activity", font=("Arial", 25)).grid(row=row, columnspan=2, sticky=tk.EW, pady=20)

        row += 1
        self.activity_name = tk.StringVar()
        tk.Label(master, text="Name:").grid(row=row, sticky=tk.W, padx=20)
        self.e1 = tk.Entry(master, textvariable=self.activity_name)
        self.e1.grid(row=row, column=1, padx=40)

        row += 1
        self.activity_type = tk.StringVar()
        tk.Label(master, text="Activity type:").grid(row=row, sticky=tk.W, padx=20)
        self.e2 = tk.Entry(master, textvariable=self.activity_type)
        self.e2.grid(row=row, column=1, padx=20)

        row += 1
        self.activity_date_due = tk.StringVar()
        tk.Label(master, text="Date due:").grid(row=row, sticky=tk.W, padx=20)
        self.e3 = tk.Entry(master, textvariable=self.activity_date_due)
        self.e3.grid(row=row, column=1, padx=20)

        row += 1
        self.activity_note = tk.StringVar()
        tk.Label(master, text="Note:").grid(row=row, sticky=tk.W, padx=20)
        self.e4 = tk.Entry(master, textvariable=self.activity_note)
        self.e4.grid(row=row, column=1, padx=20)

        row += 1
        self.activity_duration = tk.StringVar()
        tk.Label(master, text="Duration:").grid(row=row, sticky=tk.W, padx=20)
        self.e5 = tk.Entry(master, textvariable=self.activity_duration)
        self.e5.grid(row=row, column=1, padx=20)

        row += 1
        self.activity_object = tk.StringVar()
        tk.Label(master, text="Object:").grid(row=row, sticky=tk.W, padx=20)
        self.e6 = tk.Entry(master, textvariable=self.activity_object)
        self.e6.grid(row=row, column=1, padx=20)

        row += 1
        self.activity_object_id = tk.StringVar()
        tk.Label(master, text="Object ID:").grid(row=row, sticky=tk.W, padx=20)
        self.e7 = tk.Entry(master, textvariable=self.activity_object_id)
        self.e7.grid(row=row, column=1, padx=20)

        row += 1
        self.activity_assigned_to = tk.StringVar()
        tk.Label(master, text="Assigned to:").grid(row=row, sticky=tk.W, padx=20)
        self.e8 = tk.Entry(master, textvariable=self.activity_assigned_to)
        self.e8.grid(row=row, column=1, padx=20)

        row += 1
        self.activity_status = tk.StringVar()
        tk.Label(master, text="Status:").grid(row=row, sticky=tk.W, padx=20)
        self.e9 = tk.Entry(master, textvariable=self.activity_status)
        self.e9.grid(row=row, column=1, padx=20)

        row += 1
        self.button = tk.Button(master, text="Save", command=self.save)
        self.button.grid(row=row, columnspan=2, pady=20)

    @staticmethod
    def empty_string_to_none(s):
        return s if s else None

    def save(self):
        print('Saving')

        d = {
            # 'id',
            'name': self.activity_name.get(),
            'activity_type': self.activity_type.get(),
            'date_due': self.activity_date_due.get(),
            'note': self.activity_note.get(),
            'duration': self.empty_string_to_none(self.activity_duration.get()),
            'object_id': self.activity_object_id.get(),
            'object_name': self.activity_object.get(),
            'assigned_to': self.activity_assigned_to.get(),
            'date_entered': date.today(),
            'status': self.empty_string_to_none(self.activity_status.get()),
            'date_updated': datetime.now()
        }
        activity = Activity(**d)
        store_activity(activity)


if __name__ == '__main__':

    root = tk.Tk()

    # root.geometry('400x600+100+100')  # width x height + x_offset + y_offset
    root.title('Activity Tracker Input')

    app = App(root)

    root.mainloop()
