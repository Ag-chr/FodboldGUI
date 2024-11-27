from tkinter import *
from tkinter.ttk import Treeview
import pandas as pd

class listWindowClass:
    def __init__(self, master):
        self.master = master  # Reference til mainWindow-objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("Indbetalingsliste")
        self.listWindow.geometry("700x501")

        print(self.master.fodboldtur)
        fodboldturDict = {"Navn": self.master.fodboldtur.keys(), "Indbetalt": self.master.fodboldtur.values()}
        resterndelist = [self.master.dkk_pr_medlem - indbetalt for indbetalt in fodboldturDict["Indbetalt"]]
        fodboldturDict["Resterende"] = resterndelist

        self.df = pd.DataFrame.from_dict(fodboldturDict)
        self.order=True

        # Overskrift
        Label(self.listWindow, text="Indbetalingsliste").pack(pady=10)

        #Laver en tabel
        self.my_disp()

        # Tilbage til main menu knap
        Button(self.listWindow, text="Tilbage", command=self.listWindow.destroy).pack()

    def my_disp(self):
        l1 = list(self.df) # list of columns
        r_set = self.df.to_numpy().tolist()
        print("l1:", l1)
        print("r_set:", r_set)
        self.trv = Treeview(self.listWindow, selectmode='browse', show="headings", height=10, columns=l1)
        self.trv.pack()
        for col in l1:
            self.trv.column(col, width=100, anchor='w')
            self.trv.heading(col, text=col, command=lambda col=col: self.my_sort(col))
        for dt in r_set:
            v = [r for r in dt]
            self.trv.insert('', 'end', values=v)

    def my_sort(self, col):
        if self.order:
            self.order = False
        else:
            self.order = True
        self.df = self.df.sort_values([col], ascending=self.order)
        self.trv.pack_forget()
        self.my_disp()

    def FyldTabel(self):
        # Fylder tabellen  med data
        for navn, indbetalt in self.master.fodboldtur.items():
            resterende = self.master.dkk_pr_medlem - indbetalt  # Beregn resterende beløb
            self.tree.insert("", END, values=(navn, f"{indbetalt} kr", f"{resterende} kr"))


    #TODO Funktion til at sortere efter navn og indbetalt