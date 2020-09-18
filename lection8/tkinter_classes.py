# importing tkinter as tk
from tkinter import Tk, mainloop, BOTTOM
from tkinter.ttk import Button

# creating tkinter window
root = Tk()

# creting fixed size window 
root.geometry('200x150')

button = Button(root, text="Ok")
button.pack(side = BOTTOM, pady=5)

mainloop()
