from tkinter import *
from tkinter.ttk import Treeview

class listWindowClass:
    def __init__(self, master):
        self.master = master  # Reference til mainWindow-objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("Indbetalingsliste")
        self.listWindow.geometry("500x500")

        # Overskrift
        Label(self.listWindow, text="Indbetalingsliste").pack(pady=10)

        #Laver en tabel
        self.tree = Treeview(self.listWindow, columns=("Navn", "Indbetalt", "Resterende"), show="headings", height=8)
        self.tree.pack(pady=10, padx=10)

        # Tilføjer kolonneoverskrifter
        self.tree.heading("Navn", text="Navn")
        self.tree.heading("Indbetalt", text="Indbetalt")
        self.tree.heading("Resterende", text="Resterende")


        # Fyld tabellen med data
        self.FyldTabel()

        # Tilbage til main menu knap
        Button(self.listWindow, text="Tilbage", command=self.listWindow.destroy).pack()

    def FyldTabel(self):
        # Tilføj nye rækker
        for navn, beløb in self.master.fodboldtur.items():
            self.tree.insert("", END, values=(navn, f"{beløb} kr"))
