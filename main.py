# importing tkinter module
import pickle
from tkinter import *
from tkinter.ttk import * #progressbar
from tkinter import messagebox
from collections import defaultdict

from hjælpeFunktioner import gem
from listWindow import listWindowClass
from betalUdtrækWindow import payWindowClass
from worstWindow import worstWindowClass

class mainWindow:
    def __init__(self):
        self.total = 0
        self.target = 70000

        # creating tkinter window
        self.root = Tk()

        #load filen:
        self.filename = 'betalinger.pk'
        self.fodboldtur = {}

        self.fileLog = 'log.pk'
        self.log = defaultdict(list)

        try: #FILEN FINDES :)
            infile = open(self.filename, 'rb')
            self.fodboldtur = pickle.load(infile)
            infile.close()

            infile = open(self.fileLog, 'rb')
            self.log = pickle.load(infile)
            infile.close()

        except: #FILEN FINDES IKKE.
            self.fodboldtur = {"Abdi": 300, "Abdul": 3, "Abdirashid": 30000, "Abdirahim": 10000, "Zakaria": 10}
            messagebox.showerror(parent=self.root, title="SUUIIII", message="FILEN BLEV IKKE FUNDET. Derfor laves en ny")

            infile = open(self.filename, 'wb')
            pickle.dump(self.fodboldtur, infile)
            infile.close()

            infile = open(self.fileLog, 'wb')
            pickle.dump(self.log, infile)
            infile.close()


        print(self.fodboldtur)
        self.total = sum(self.fodboldtur.values())
        print(f"TOTAL: {self.total}")


        #TEXT:
        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)

        # Progress bar widget
        self.progressLabelText = StringVar()
        self.progressLabelText.set(f"Indsamlet: {self.total} af {self.target} kroner:")

        self.progressLabel = Label(self.root, textvariable=self.progressLabelText)
        self.progressLabel.pack()
        self.progress = Progressbar(self.root, orient = HORIZONTAL,
                    length = 250, mode = 'determinate')
        self.progress['value'] = self.total/self.target*100
        #print(self.progress['length'])
        #print(self.progress['value'])

        #BUTTONS
        self.progress.pack(padx= 20)

        listButton = Button(self.root,text ="Liste over indbetalinger",command = lambda: listWindowClass(self))
        listButton.pack(padx = 20, pady = 10,side=LEFT)


        payButton = Button(self.root,text ="Indbetal",command = lambda: payWindowClass(self))
        payButton.pack(padx = 20, pady = 10,side=LEFT)

        bottom3Button = Button(self.root,text ="Bund 3",command = lambda: worstWindowClass(self))
        bottom3Button.pack(padx = 20, pady = 10,side=LEFT)

        # infinite loop
        mainloop()
    def gemFilen(self):
        gem(self.filename, self.fodboldtur)
        gem(self.fileLog, self.log)
        print("GEMT")

if __name__ == '__main__':
    main = mainWindow()

print("Nicolas Jackson In Action With The Cold Reaction")
