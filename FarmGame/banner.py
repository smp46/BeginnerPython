# Import required libraries
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog # For masters task
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry(f'{FARM_WIDTH + INVENTORY_WIDTH}x{FARM_WIDTH + INFO_BAR_HEIGHT + BANNER_HEIGHT}')

frame = Frame(win, width=FARM_WIDTH + INVENTORY_WIDTH, height=BANNER_HEIGHT)
frame.pack()
frame.place(anchor='n', relx=0.5, rely=0)

# Create an object of tkinter ImageTk
banner_size = (FARM_WIDTH + INVENTORY_WIDTH, BANNER_HEIGHT)
img = get_image('images/header.png', banner_size)

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

win.mainloop()