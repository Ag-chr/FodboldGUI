# importing tkinter module
from tkinter import *
from tkinter import messagebox



class payWindowClass:

    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")

        # Top
        Label(self.payWindow, text="Indbetal eller udtræk").pack(side=TOP)

        # Bottom

        Button(self.payWindow, text="Tilbage", command=self.payWindow.destroy).pack(side=BOTTOM)

        scrollbar = Scrollbar(self.payWindow)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.logList = Listbox(self.payWindow, yscrollcommand=scrollbar.set)
        self.logList.pack(side=BOTTOM)

        scrollbar.config(command=self.logList.yview)
        Label(self.payWindow, text="Log").pack(side=BOTTOM)

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
        self.drop.pack(side=LEFT, fill=BOTH, expand=True)

        Label(self.payWindow, text="Skriv beløb:").pack(side=LEFT, fill=BOTH)

        self.moneyEntry = Entry(self.payWindow)
        self.moneyEntry.pack(side=LEFT, fill=BOTH, expand=True)

        Label(self.payWindow, text="kr.").pack(side=LEFT, fill=BOTH)

        self.button = Button(self.payWindow, text="betal", command=lambda: self.addMoney(self.validere_beløb(self.moneyEntry.get())))
        self.button.pack(side=LEFT, fill=BOTH, expand=True)

        self.button = Button(self.payWindow, text="udtræk", command=lambda: self.addMoney(-self.validere_beløb(self.moneyEntry.get())))
        self.button.pack(side=LEFT, fill=BOTH, expand=True)

    def addMoney(self, amount):
        person = self.valgtPerson.get()

        if person not in self.master.fodboldtur:
            messagebox.showerror(parent=self.payWindow, title="SUUIIII", message="Vælg en person")

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

        self.logList.delete(0, END)
        personLog = self.master.log[person]
        for mængde in personLog:
            self.logList.insert(END, mængde)

    def updateLog(self, person, beløb):
        self.master.log[person].insert(0, beløb)




