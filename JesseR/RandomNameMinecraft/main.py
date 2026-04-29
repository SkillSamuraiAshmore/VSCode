###
# Author: Jesse Read
# Date: 28/03/2028
# Information: Random name generator. Used to select a student for prize. 
#              Edit names_list on line 15 to include student names. Name removed is
#              once a student has won. Only displays two names in total.
###
import tkinter as tk
import random
from PIL import Image, ImageTk
import time
import pygame
import threading

# Create a list of names
names_list = ["Ashton", "Isabella", "Massimo", "Jordan", "Christian", "Ruby", "Ryker", "Lotte", "Oliver", "Aiden", "Gideon" ]

# Function to select a random name and display it
def show_random_name():
    cycle_names(50)
    
def cycle_names(iterations):
    if iterations > 0:
        name = random.choice(names_list)  # Pick a random name
        label.config(text=name)  # Update the label
        # Schedule the next name change with a small delay
        root.after(50, cycle_names, iterations - 1)  # Delay of 100ms before next change
    else:
        # Optionally do something when all names have cycled (e.g., show the final name)
        #label.config(text="Done!")  # Final message after cycling
        showWinText()

# Set up the main window
root = tk.Tk()
root.title("Random Name Picker")

# Set window size and background
root.geometry("1280x720")
background_image = Image.open(r"C:\repos\VSCode\JesseR\RandomNameMinecraft\background.jpg")  # Replace with your image path
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

button = tk.Button(
        root, 
        text="Pick a Name", 
        font=("Helvetica", 16), 
        bg="#6E4D32",  # Brown like wood or dirt
        fg="white",  # White text for contrast
        bd=5,  # Thick border
        relief="ridge",  # Gives it a blocky, 3D feel
        command=show_random_name
    )
button.pack(pady=(280, 20))

# Label to display the random name
label = tk.Label(root, text="", font=("Helvetica", 32), bg="Antiquewhite1", fg="black",relief="ridge",)
label.pack(pady=50)




def showWinText():
    # Button to generate a random name
    label_winner = tk.Label(root, text=label.cget("text")+" is a Winner!", font=("Helvetica", 24), bg="chartreuse3", fg="white", relief="ridge",)
    label_winner.pack(pady=25)
    removeWinnersName(label.cget("text"))
    
def removeWinnersName(name):
    names_list.remove(name)

# Run the GUI
root.mainloop()
