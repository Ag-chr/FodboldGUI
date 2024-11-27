from tkinter import *
from tkinter.ttk import Treeview
import pandas as pd
from hjælpeFunktioner import MakeTree

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
        self.l1 = list(self.df)  # list of columns
        self.order = True

        # Overskrift
        Label(self.listWindow, text="Indbetalingsliste").pack(pady=10)

        self.trv = MakeTree(self.listWindow, self.df)
        self.trv.my_disp()

        # Tilbage til main menu knap
        Button(self.listWindow, text="Tilbage", command=self.listWindow.destroy).pack()

    def FyldTabel(self):
        # Fylder tabellen  med data
        for navn, indbetalt in self.master.fodboldtur.items():
            resterende = self.master.dkk_pr_medlem - indbetalt  # Beregn resterende beløb
            self.tree.insert("", END, values=(navn, f"{indbetalt} kr", f"{resterende} kr"))


    #TODO Funktion til at sortere efter navn og indbetalt