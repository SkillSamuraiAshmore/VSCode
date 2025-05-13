import tkinter as tk
import random
from PIL import Image, ImageTk
import time
import pygame
import threading

# Create a list of names
names_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]

# Function to select a random name and display it
def show_random_name():
    cycle_names(20)
    
def cycle_names(iterations):
    if iterations > 0:
        name = random.choice(names_list)  # Pick a random name
        label.config(text=name)  # Update the label
        # Schedule the next name change with a small delay
        root.after(100, cycle_names, iterations - 1)  # Delay of 100ms before next change
    else:
        # Optionally do something when all names have cycled (e.g., show the final name)
        label.config(text="Done!")  # Final message after cycling

# Set up the main window
root = tk.Tk()
root.title("Random Name Picker")

# Set window size and background
root.geometry("800x350")
background_image = Image.open("C:\\repos\\VSCode-1\\JesseR\\RandomNameMinecraft\\background.jpg")  # Replace with your image path
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Label to display the random name
label = tk.Label(root, text="", font=("Helvetica", 24), bg="white", fg="black")
label.pack(pady=50)

# Button to generate a random name
button = tk.Button(root, text="Pick a Name", font=("Helvetica", 16), command=show_random_name)
button.pack(pady=20)

# Run the GUI
root.mainloop()
