import tkinter as tk

class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)





def main():
    root = tk.Tk()
    root.geometry('600x500+300+300')  # width x height + x_offset + y_offset
    root.resizable(width = False, height = False)
    root.title('My GUI')
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
