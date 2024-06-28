import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# List of options 
options = ["GitHub", "Slack", "HackClub", "Arcade", "Nothing"]
image_files = {
    "GitHub": "github.png",
    "Slack": "slack.png",
    "HackClub": "hackclub.png",
    "Arcade": "arcade.png",
    "Nothing": "nothing.jpeg"
}

# Randomly choose the correct answer
correct_answer = random.choice(options)

# Function to check the user's guess
def check_guess(user_guess):
    global correct_answer
    if user_guess == correct_answer:
        show_image(image_files[user_guess])
        messagebox.showinfo("Result", "Congratulations! You guessed it right.")
    else:
        messagebox.showinfo("Result", f"Sorry, the correct answer was {correct_answer}.")
        # Reset the game with a new random answer
        correct_answer = random.choice(options)

# Function to show the image
def show_image(image_file):
    image = Image.open(image_file)
    image = ImageTk.PhotoImage(image)
    image_label.config(image=image)
    image_label.image = image 


root = tk.Tk()
root.title("Guess the Option Game")


instruction_label = tk.Label(root, text="Guess the correct option:")
instruction_label.pack(pady=10)


image_label = tk.Label(root)
image_label.pack(pady=10)

for option in options:
    option_button = tk.Button(root, text=option, command=lambda opt=option: check_guess(opt))
    option_button.pack(pady=5)


root.mainloop()
