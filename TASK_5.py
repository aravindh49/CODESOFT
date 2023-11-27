import tkinter as tk
from tkinter import ttk, messagebox

# Create main window
root = tk.Tk()
root.title("Contact Book")

# Set window size and background color
root.geometry("400x400")
root.configure(bg='light blue')

# Create a dictionary to store contacts
contacts = {}

# Function to add contact
def add_contact():
    name = name_entry.get()
    number = number_entry.get()
    if name and number:
        contacts[name] = number
        update_contacts()
        name_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Both fields are required")

# Function to update contacts listbox
def update_contacts():
    contacts_listbox.delete(0, tk.END)
    for name, number in contacts.items():
        contacts_listbox.insert(tk.END, name + ": " + number)

# Create labels, entries, and buttons with styling
style = ttk.Style()
style.configure("TButton", font=('Arial', 14), bg='light blue', fg='black')

name_label = tk.Label(root, text="Name", bg='light blue', font=('Arial', 14))
name_entry = ttk.Entry(root, font=('Arial', 14))
number_label = tk.Label(root, text="Number", bg='light blue', font=('Arial', 14))
number_entry = ttk.Entry(root, font=('Arial', 14))
add_button = ttk.Button(root, text="Add Contact", command=add_contact)
contacts_listbox = tk.Listbox(root, font=('Arial', 14))

# Grid layout
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry.grid(row=0, column=1, padx=10, pady=10)
number_label.grid(row=1, column=0, padx=10, pady=10)
number_entry.grid(row=1, column=1, padx=10, pady=10)
add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
contacts_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start main loop
root.mainloop()
