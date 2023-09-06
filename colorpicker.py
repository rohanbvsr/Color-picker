from tkinter import *
from tkinter import colorchooser  # Import the colorchooser module

a = Tk()

def mcolor():
    color = colorchooser.askcolor()[1]  # Use [1] to get the background color from the returned tuple
    label = Label(text=f'Your chosen color: {color}', bg=color)  # Set the background color of the label
    label.pack()

button = Button(text="Choose color", width=30, command=mcolor)
button.pack()

a.mainloop()
