import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# Function to generate password
def generate_password():
    length = length_entry.get()
    if length.isdigit() and int(length) > 0:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(int(length)))
        password_text.set(password)
    else:
        messagebox.showerror("Error", "Please enter a valid number")

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Set window size and background color
root.geometry("400x200")
root.configure(bg='light blue')

# Create StringVar for password text
password_text = tk.StringVar()
password_text.set("Your password will appear here")

# Create label, entry, and button with styling
style = ttk.Style()
style.configure("TButton", font=('Arial', 14), bg='light blue', fg='black')

length_label = tk.Label(root, text="Password Length", bg='light blue', font=('Arial', 14))
length_entry = ttk.Entry(root, font=('Arial', 14))
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
password_label = tk.Label(root, textvariable=password_text, bg='light blue', font=('Arial', 14))

# Grid layout
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start main loop
root.mainloop()
