import tkinter as tk


class App(tk.Tk):
    def add(self):
        if self.e_input.get() not in self.values:
            self.values.append(self.e_input.get())
            self.l_answers.insert(tk.END, self.e_input.get())

    def delete(self):
        for i in reversed(self.l_answers.curselection()):
            text = self.l_answers.get(i)
            self.values.remove(text)
            self.l_answers.delete(i)

    def __init__(self):
        super().__init__()

        self.configure(background='#ffffff')
        self.title('To DO list')
        self.grid_columnconfigure(1, weight=1)

        self.values = []

        self.l_input = tk.Label(self, text='Input', justify=tk.CENTER, bd=2)
        self.e_input = tk.Entry(self, justify=tk.RIGHT, bd=2)
        self.e_btn_add = tk.Button(self, text='ADD', bg='#30d5c8', command=self.add)
        self.l_answers = tk.Listbox(self, justify=tk.CENTER, bd=2)
        self.e_btn_del = tk.Button(self, text='DELETE', command=self.delete)

        self.l_input.grid(column=0, row=0, sticky="WESN")
        self.e_input.grid(column=1, row=0, sticky="WESN")
        self.e_btn_add.grid(column=0, row=1, columnspan=2, sticky="WESN")
        self.l_answers.grid(column=1, columnspan=2, row=2, sticky="WESN")
        self.e_btn_del.grid(column=1, columnspan=2, row=3, sticky="WESN")


if __name__ == '__main__':
    my_app = App()
    my_app.mainloop()
