import tkinter as tk
from tkinter import simpledialog


class NameEditorApp:
    def __init__(self, parent, fodboldtur):
        self.parent = parent
        self.fodboldtur = fodboldtur
        self.names = list(fodboldtur.keys())  # Extract names from `fodboldtur`
        self.dkk_pr_medlem = parent.dkk_pr_medlem  # Get price from the main window

        # Create new window
        self.window = tk.Toplevel(parent.root)
        self.window.title("Indstillinger")

        # Get screen resolution to scale the window
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Set the window to fill the screen
        self.window.geometry(f"{screen_width}x{screen_height}")
        self.window.config(padx=10, pady=10)  # Reduced padding around window

        # Title Label
        self.title_label = tk.Label(self.window, text="Indstillinger", font=("Helvetica", 30))
        self.title_label.place(x=screen_width//2 - 100, y=40, anchor="center")

        # Add New Member Section
        self.add_name_label = tk.Label(self.window, text="Tilføj Ny Medlem:", font=("Helvetica", 18))
        self.add_name_label.place(x=screen_width//5, y=120)

        self.add_name_entry = tk.Entry(self.window, font=("Helvetica", 18), width=20)
        self.add_name_entry.place(x=screen_width//5, y=160)

        self.add_button = tk.Button(self.window, text="Tilføj", font=("Helvetica", 18), command=self.add_name)
        self.add_button.place(x=screen_width//5, y=200)

        # Members List Section
        self.members_label = tk.Label(self.window, text="Medlemmer", font=("Helvetica", 18))
        self.members_label.place(x=screen_width//2, y=120)

        # Create a frame to hold the Listbox and the Scrollbar
        self.list_frame = tk.Frame(self.window)
        self.list_frame.place(x=screen_width//2 - 100, y=160)

        # Create a Canvas widget for scrolling
        self.canvas = tk.Canvas(self.list_frame, height=200, width=300)
        self.canvas.grid(row=0, column=0, padx=5, pady=5)

        # Create a Scrollbar linked to the canvas
        self.scrollbar = tk.Scrollbar(self.list_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Create a Listbox inside the canvas
        self.listbox_frame = tk.Frame(self.canvas)
        self.listbox = tk.Listbox(self.listbox_frame, font=("Helvetica", 18), height=10, width=30)
        self.listbox.pack()

        # Configure the scrollbar and canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.listbox_frame, anchor="nw")
        self.listbox_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        # Bind double-click event to edit member names
        self.name_listbox = self.listbox
        self.name_listbox.bind("<Double-1>", self.edit_name)

        # Delete button
        self.delete_button = tk.Button(self.window, text="Slet", font=("Helvetica", 18), command=self.delete_member)
        self.delete_button.place(x=screen_width//2 - 50, y=350)

        # Price per Member Section
        self.price_label = tk.Label(self.window, text="Pris pr medlem:", font=("Helvetica", 18))
        self.price_label.place(x=screen_width*3/4, y=120)

        self.price_value_label = tk.Label(self.window, text=f"{self.dkk_pr_medlem} DKK", font=("Helvetica", 18))
        self.price_value_label.place(x=screen_width*3/4, y=160)

        self.edit_price_button = tk.Button(self.window, text="Rediger pris", font=("Helvetica", 18), command=self.edit_price)
        self.edit_price_button.place(x=screen_width*3/4, y=200)

        # Back button (Gem og Luk)
        self.back_button = tk.Button(self.window, text="Gem og Luk", font=("Helvetica", 18), command=self.close_window)
        self.back_button.place(x=screen_width//2, y=screen_height - 100, anchor="center")

        # Populate listbox with current names
        self.update_listbox()

        # Allow resizing of the window
        self.window.resizable(True, True)

    def update_listbox(self):
        """Update the listbox with current names"""
        self.name_listbox.delete(0, tk.END)
        for name in self.names:
            self.name_listbox.insert(tk.END, name)

    def add_name(self):
        """Add a new name to the list"""
        name = self.add_name_entry.get()
        if name and name not in self.fodboldtur:
            self.fodboldtur[name] = 0  # Add the name with initial payment 0
            self.names.append(name)
            self.update_listbox()
            self.parent.gemFilen()  # Save updated data to file
        self.add_name_entry.delete(0, tk.END)

    def edit_name(self, event):
        """Edit an existing name"""
        selected = self.name_listbox.curselection()
        if selected:
            old_name = self.name_listbox.get(selected)
            new_name = simpledialog.askstring("Rediger navn", f"Ændr navn '{old_name}':", initialvalue=old_name)
            if new_name and new_name not in self.fodboldtur:
                self.fodboldtur[new_name] = self.fodboldtur.pop(old_name)  # Rename in fodboldtur
                self.names[selected[0]] = new_name
                self.update_listbox()
                self.parent.gemFilen()  # Save updated data to file

    def delete_member(self):
        """Remove selected member from the list"""
        selected = self.name_listbox.curselection()
        if selected:
            member_name = self.name_listbox.get(selected)
            del self.fodboldtur[member_name]  # Delete from fodboldtur
            self.names.remove(member_name)
            self.update_listbox()
            self.parent.gemFilen()  # Save updated data to file

    def edit_price(self):
        """Edit the price per member"""
        new_price = simpledialog.askinteger("Rediger pris", "Indtast ny pris pr medlem:", initialvalue=self.dkk_pr_medlem)
        if new_price is not None:
            self.dkk_pr_medlem = new_price
            self.price_value_label.config(text=f"{self.dkk_pr_medlem} DKK")
            # After editing the price, update the progress bar in the main window
            self.parent.dkk_pr_medlem = self.dkk_pr_medlem
            self.parent.update_target()  # Recalculate target and update progress bar

    def close_window(self):
        """Save data and close the window"""
        self.parent.update_target()  # Update the progress bar in the main window
        self.parent.gemFilen()  # Save data to file
        self.window.destroy()
