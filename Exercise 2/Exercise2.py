# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 08:47:30 2024

@author: User
"""

import tkinter as tk
import random

# In this function the jokes are generated when the user clicks on alexa, tell me a joke.
def load_jokes():
    jokes = []
    with open('RandomJokes.txt', 'r') as file:
        for line in file:
            setup, punchline = line.strip().split('?')
            jokes.append((setup + '?', punchline))
    return jokes

# Function to display the setup of a random joke
def display_setup():
    global current_joke
    current_joke = random.choice(jokes)
    setup_label.config(text=current_joke[0])
    punchline_label.config(text="")  # Clear previous punchline
    punchline_button.config(state=tk.NORMAL)  # Enable punchline button

# Function to display the punchline of the current joke
def display_punchline():
    punchline_label.config(text=current_joke[1])
    punchline_button.config(state=tk.DISABLED)  # Disable punchline button

# Exit the program
def quit_program():
    window.quit()

# Initialize the jokes and GUI
jokes = load_jokes()
window = tk.Tk()
window.geometry("500x500")
window.title("Alexa, Tell Me a Joke")

# Setup the joke display area
setup_label = tk.Label(window, text="", font=("Arial", 14), wraplength=300)
setup_label.pack(pady=20)

# Punchline display
punchline_label = tk.Label(window, text="", font=("Arial", 14), wraplength=300)
punchline_label.pack(pady=10)

# Button to show the punchline
punchline_button = tk.Button(window, text="Show Punchline", command=display_punchline, state=tk.DISABLED)
punchline_button.pack(pady=5)

# Button to get a new joke
new_joke_button = tk.Button(window, text="Alexa, tell me a joke", command=display_setup)
new_joke_button.pack(pady=5)

# Quit button
quit_button = tk.Button(window, text="Quit", command=quit_program)
quit_button.pack(pady=20)

# Start the program
window.mainloop()
