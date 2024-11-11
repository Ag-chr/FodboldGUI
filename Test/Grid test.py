import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Main Window")

# Function to create a Toplevel window with grid layout
def open_toplevel():
    # Create a new Toplevel window
    top = tk.Toplevel(root)
    top.title("Toplevel with Grid")

    # Configure the grid
    #top.columnconfigure(0, weight=1)
    #top.columnconfigure(1, weight=1)

    # Add widgets to the Toplevel window using grid
    label1 = tk.Label(top, text="Label 1")
    label1.grid(row=0, column=0, padx=10, pady=10)

    label2 = tk.Label(top, text="Label 2")
    label2.grid(row=0, column=1, padx=10, pady=10)

    button1 = tk.Button(top, text="Button 1")
    button1.grid(row=1, column=0, padx=10, pady=10)

    button2 = tk.Button(top, text="Button 2")
    button2.grid(row=1, column=1, padx=10, pady=10)

# Button in the main window to open the Toplevel window
open_button = tk.Button(root, text="Open Toplevel Window", command=open_toplevel)
open_button.pack(pady=20)

# Start the main event loop
root.mainloop()
