from tkinter import *
from tkinter.ttk import Treeview
import pandas as pd

class listWindowClass:
    def __init__(self, master):
        self.master = master  # Reference til mainWindow-objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("Indbetalingsliste")
        self.listWindow.geometry("700x501")

        fodboldturDict = {}
        fodboldturDict["Navn"] = self.master.fodboldtur.keys()
        fodboldturDict["Indbetalt"] = self.master.fodboldtur.values()
        fodboldturDict["Resterende"] = [self.master.dkk_pr_medlem - indbetalt for indbetalt in fodboldturDict["Indbetalt"]]

        self.df = pd.DataFrame.from_dict(fodboldturDict)
        self.order=True
        self.l1 = list(self.df)  # list of columns

        # Overskrift
        Label(self.listWindow, text="Indbetalingsliste").pack(pady=10)

        self.trv = Treeview(self.listWindow, selectmode='browse', show="headings", height=10, columns=self.l1)
        self.trv.pack()
        #Laver en tabel
        self.my_disp()

        # Tilbage til main menu knap
        Button(self.listWindow, text="Tilbage", command=self.listWindow.destroy).pack()

    def my_disp(self):
        r_set = self.df.to_numpy().tolist()
        for col in self.l1:
            self.trv.column(col, width=200, anchor='w')
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
        self.trv.delete(*self.trv.get_children())
        self.my_disp()

    def FyldTabel(self):
        # Fylder tabellen  med data
        for navn, indbetalt in self.master.fodboldtur.items():
            resterende = self.master.dkk_pr_medlem - indbetalt  # Beregn resterende beløb
            self.tree.insert("", END, values=(navn, f"{indbetalt} kr", f"{resterende} kr"))


    #TODO Funktion til at sortere efter navn og indbetalt