import tkinter as tk


class App(tk.Frame):

    def __init__(self, master=None):

        w = tk.Label(master, text='Hello, world!', fg='darkred')
        w.grid()

        self.txt_content = tk.StringVar()
        txt = tk.Entry(master, textvariable=self.txt_content)
        txt.grid()

        btn = tk.Button(master, text='Klik here!', command=self.button_handler)
        btn.grid()

    def button_handler(self):
        s = self.txt_content.get()
        print(s)


if __name__ == '__main__':

    root = tk.Tk()

    root.geometry('300x200')  # width x height + x_offset + y_offset
    root.title('tkinter demo')

    app = App(root)

    root.mainloop()
