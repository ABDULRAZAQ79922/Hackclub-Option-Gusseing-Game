import tkinter as tk
from tkinter import messagebox
import random

# List of options
options = ["GitHub", "Slack", "HackClub", "Arcade", "Nothing"]

# Randomly choose the correct answer
correct_answer = random.choice(options)

# Function to check the user's guess
def check_guess(user_guess):
    global correct_answer
    if user_guess == correct_answer:
        messagebox.showinfo("Result", "Congratulations! You guessed it right.")
    else:
        messagebox.showinfo("Result", f"Sorry, the correct answer was {correct_answer}.")
    # Reset the game with a new random answer
    correct_answer = random.choice(options)

# Create the main window
root = tk.Tk()
root.title("Guess the Option Game")

# Create a label to display instructions
instruction_label = tk.Label(root, text="Guess the correct option:")
instruction_label.pack(pady=10)

# Create buttons for each option
for option in options:
    option_button = tk.Button(root, text=option, command=lambda opt=option: check_guess(opt))
    option_button.pack(pady=5)

# Run the GUI event loop
root.mainloop()
