# importing tkinter module
from tkinter import *
from tkinter import messagebox



class payWindowClass:

    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")

        Label(self.payWindow,
              text="Indbetal eller udtræk").grid(row=0, column=0, padx=10, pady=10, columnspan=10)

        self.valgtPerson = StringVar()
        #TODO: sortere liste alfabetisk
        self.options = [p for p in self.master.fodboldtur]
        self.valgtPerson.set("Vælg person")

        # row 1
        self.drop = OptionMenu(self.payWindow, self.valgtPerson, *self.options)
        self.drop.grid(row=1, column=0, pady=10)

        Label(self.payWindow, text="Skriv beløb:").grid(row=1, column=1, pady=10)

        self.moneyEntry = Entry(self.payWindow)
        self.moneyEntry.grid(row=1, column=2, pady=10, columnspan=3)

        Label(self.payWindow, text="kr.").grid(row=1, column=5, pady=10)

        # row 2
        self.button = Button(self.payWindow, text="betal", command=lambda: self.addMoney(self.validere_beløb(self.moneyEntry.get())))
        self.button.grid(row=2, column=2, padx=10, pady=10)

        self.button = Button(self.payWindow, text="udtræk", command=lambda: self.addMoney(-self.validere_beløb(self.moneyEntry.get())))
        self.button.grid(row=2, column=4, padx=10, pady=10)

    def addMoney(self, amount):
        if self.valgtPerson.get() not in self.master.fodboldtur:
            messagebox.showerror(parent=self.payWindow, title="SUUIIII", message="Vælg en person")

        self.master.fodboldtur[self.valgtPerson.get()] += amount
        self.master.total += amount
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100
        ##TODO: TELL MAIN WINDOW TO PICKLE THE DICTIONARY
        print(self.master.fodboldtur)
        self.master.gemFilen()

    def validere_beløb(self, input):
        try:
            input = abs(int(input))
        except:
            messagebox.showerror(parent=self.payWindow, title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return "FEJL"
        return input
