import tkinter as tk
from tkinter import ttk, messagebox

# Function to add task
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a task")

# Function to delete task
def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showerror("Error", "Please select a task to delete")

# Function to update task
def update_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        new_task = task_entry.get()
        if new_task:
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task")
    else:
        messagebox.showerror("Error", "Please select a task to update")

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Set window size and background color
root.geometry("300x400")
root.configure(bg='light blue')

# Create label, entry, and buttons with styling
style = ttk.Style()
style.configure("TButton", font=('Arial', 14), bg='light blue', fg='black')

task_label = tk.Label(root, text="Task", bg='light blue', font=('Arial', 14))
task_entry = ttk.Entry(root, font=('Arial', 14))
add_button = ttk.Button(root, text="Add Task", command=add_task)
delete_button = ttk.Button(root, text="Delete Task", command=delete_task)
update_button = ttk.Button(root, text="Update Task", command=update_task)
tasks_listbox = tk.Listbox(root, font=('Arial', 14))

# Grid layout
task_label.grid(row=0, column=0, padx=10, pady=10)
task_entry.grid(row=0, column=1, padx=10, pady=10)
add_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
delete_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
update_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
tasks_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start main loop
root.mainloop()
