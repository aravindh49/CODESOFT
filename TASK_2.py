import tkinter as tk
from tkinter import ttk

# Function to perform calculation
def calculate():
    num1 = num1_entry.get()
    num2 = num2_entry.get()
    operator = operator_combobox.get()

    if num1.isdigit() and num2.isdigit() and operator in ['+', '-', '*', '/']:
        if operator == '+':
            result = int(num1) + int(num2)
        elif operator == '-':
            result = int(num1) - int(num2)
        elif operator == '*':
            result = int(num1) * int(num2)
        else:  # operator == '/'
            if int(num2) != 0:
                result = int(num1) / int(num2)
            else:
                return
        result_label.config(text=str(result))

# Create main window
root = tk.Tk()
root.title("Calculator")

# Create labels, entries, and button with styling
style = ttk.Style()
style.configure("TButton", font=('Arial', 14), bg='light blue', fg='black')

num1_label = tk.Label(root, text="Number 1", bg='light blue', font=('Arial', 14))
num1_entry = ttk.Entry(root, font=('Arial', 14))
num2_label = tk.Label(root, text="Number 2", bg='light blue', font=('Arial', 14))
num2_entry = ttk.Entry(root, font=('Arial', 14))
operator_label = tk.Label(root, text="Operator", bg='light blue', font=('Arial', 14))
operator_combobox = ttk.Combobox(root, values=['+', '-', '*', '/'], font=('Arial', 14))
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
result_label = tk.Label(root, text="", bg='light blue', font=('Arial', 14))

# Grid layout
num1_label.grid(row=0, column=0, padx=10, pady=10)
num1_entry.grid(row=0, column=1, padx=10, pady=10)
num2_label.grid(row=1, column=0, padx=10, pady=10)
num2_entry.grid(row=1, column=1, padx=10, pady=10)
operator_label.grid(row=2, column=0, padx=10, pady=10)
operator_combobox.grid(row=2, column=1, padx=10, pady=10)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start main loop
root.mainloop()
