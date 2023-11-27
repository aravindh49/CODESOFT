import tkinter as tk
import random
from tkinter import ttk

# Function to choose winner
def choose_winner(user_choice):
    choices = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(choices)
    comp_choice_text.set("Computer chose: " + comp_choice)

    if user_choice == comp_choice:
        result_text.set("It's a tie!")
    elif (user_choice == 'rock' and comp_choice == 'scissors') or \
         (user_choice == 'paper' and comp_choice == 'rock') or \
         (user_choice == 'scissors' and comp_choice == 'paper'):
        result_text.set("You win!")
    else:
        result_text.set("You lose!")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Set window size and background color
root.geometry("300x200")
root.configure(bg='light blue')

# Create StringVar for result text and computer's choice
result_text = tk.StringVar()
result_text.set("Choose rock, paper, or scissors")
comp_choice_text = tk.StringVar()
comp_choice_text.set("")

# Create buttons with styling
style = ttk.Style()
style.configure("TButton", font=('Arial', 14), bg='light blue', fg='black')

rock_button = ttk.Button(root, text="Rock", command=lambda: choose_winner('rock'))
paper_button = ttk.Button(root, text="Paper", command=lambda: choose_winner('paper'))
scissors_button = ttk.Button(root, text="Scissors", command=lambda: choose_winner('scissors'))

# Create labels for result text and computer's choice with styling
result_label = tk.Label(root, textvariable=result_text, bg='light blue', font=('Arial', 14))
comp_choice_label = tk.Label(root, textvariable=comp_choice_text, bg='light blue', font=('Arial', 14))

# Grid layout
rock_button.grid(row=0, column=0, padx=10, pady=10)
paper_button.grid(row=0, column=1, padx=10, pady=10)
scissors_button.grid(row=0, column=2, padx=10, pady=10)
result_label.grid(row=1, column=0, columnspan=3)
comp_choice_label.grid(row=2, column=0, columnspan=3)

# Start main loop
root.mainloop()
