import pickle


def gem(filename, item):
    outfile = open(filename, 'wb')
    pickle.dump(item, outfile)
    outfile.close()


def moneySortedList():
    return dict(sorted(fodboldtur.items(), key=lambda item: item[1]))

def nameSortedList():
    pass

from tkinter import *
from tkinter.ttk import Treeview
import pandas as pd
class MakeTree:
    def __init__(self, master, df: pd.DataFrame):
        self.master = master
        self.df = df
        self.l1 = list(self.df)  # list of columns
        self.order = True

        self.trv = Treeview(self.master, selectmode='browse', show="headings", height=10, columns=self.l1)
        self.trv.pack()

    # fylder tabel med information
    def my_disp(self):
        r_set = self.df.to_numpy().tolist()
        for col in self.l1:
            self.trv.column(col, width=200, anchor='w')
            self.trv.heading(col, text=col, command=lambda col=col: self.my_sort(col)) # col=col gør så den sortere. Ellers virker det ikke
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

