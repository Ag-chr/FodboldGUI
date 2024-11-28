# importing tkinter module
from tkinter import *
from tkinter import messagebox
import time

from hjælpeFunktioner import MakeTree
import pandas as pd

class payWindowClass:

    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")

        # Top
        Label(self.payWindow, text="Indbetal eller udtræk").pack(side=TOP)

        # Bottom

        Button(self.payWindow, text="Tilbage", command=self.payWindow.destroy).pack(side=BOTTOM)

        self.trv = MakeTree(self.payWindow, pd.DataFrame.from_dict({"Beløb": [], "Dato": []}), BOTTOM)

        self.personMoney = StringVar()
        self.personMoney.set("Beløb indbetalt: ---")

        self.personMoneyLabel = Label(self.payWindow, text=self.personMoney.get())
        self.personMoneyLabel.pack(side=BOTTOM)

        # Left
        self.valgtPerson = StringVar()
        # TODO: sortere liste alfabetisk
        self.options = sorted([p for p in self.master.fodboldtur])
        self.valgtPerson.set("Vælg person")

        self.drop = OptionMenu(self.payWindow, self.valgtPerson, *self.options, command=lambda person: self.updateInfo(person))
        self.drop.pack(side=LEFT, fill=X, expand=True)

        Label(self.payWindow, text="Skriv beløb:").pack(side=LEFT, fill=BOTH)

        self.moneyEntry = Entry(self.payWindow)
        self.moneyEntry.pack(side=LEFT, fill=BOTH, expand=True)

        Label(self.payWindow, text="kr.").pack(side=LEFT, fill=X)

        self.button = Button(self.payWindow, text="betal", command=lambda: self.addMoney(self.validere_beløb(self.moneyEntry.get())))
        self.button.pack(side=LEFT, fill=X, expand=True)

        self.button = Button(self.payWindow, text="udtræk", command=lambda: self.addMoney(-self.validere_beløb(self.moneyEntry.get())))
        self.button.pack(side=LEFT, fill=X, expand=True)

    def addMoney(self, amount):
        person = self.valgtPerson.get()

        if person not in self.master.fodboldtur:
            messagebox.showerror(parent=self.payWindow, title="SUUIIII", message="Vælg en person")
            return
        elif self.master.fodboldtur[person] + amount < 0:
            amount = -self.master.fodboldtur[person]
        elif self.master.fodboldtur[person] + amount == 0:
            return

        self.master.fodboldtur[person] += amount
        self.master.total += amount
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        self.master.progress['value'] = self.master.total / self.master.target * 100

        self.updateLog(person, amount)
        self.updateInfo(person)

        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        print(self.master.fodboldtur)
        self.master.gemFilen()

    def validere_beløb(self, input):
        try:
            input = abs(int(input))
        except:
            messagebox.showerror(parent=self.payWindow, title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return "FEJL"
        return input

    def updateInfo(self, person):
        self.personMoney.set(f"Beløb indbetalt: {self.master.fodboldtur[person]}")
        self.personMoneyLabel.configure(text=self.personMoney.get())

        personLog =self.master.log[person]
        temp = {"Beløb": [], "Dato": []}
        for line in personLog:
            temp["Beløb"].append(line[0])
            temp["Dato"].append(line[1])

        self.trv.df = pd.DataFrame.from_dict(temp)
        self.trv.my_disp()

    def updateLog(self, person, beløb):
        self.master.log[person].insert(0, (beløb, time.strftime("%H:%M | %Y-%m-%d", time.localtime())))




