'''
Created on Mar 26, 2017

@author: Austin Dillinger
'''

import tkinter as tk

from getstyle import getstyle
from getabv import getabv
from getbeerdate import getbeerdate
from gettemperature import gettemperature
#from PIL import ImageTk, Image


SIDE_ONE = "Shower Hop"
SIDE_TWO = "Shower Hop"

DEFAULT_FONT = ("FontAwesome Regular", 12)

ROOT = tk.Tk()
ROOT.geometry("480x320")
ROOT.title("Keg-O-View")

#img = ImageTk.PhotoImage(Image.open("D:\\Pictures\\row1_keg.png"))

BACKGROUND_FILE = tk.PhotoImage(file="D:\\Pictures\\kegs.png")
BACKGROUND_LABEL = tk.Label(ROOT, image=BACKGROUND_FILE)
BACKGROUND_LABEL.place(x=0, y=0, relwidth=1, relheight=1)

FRAME = tk.Frame(ROOT)


FRAME.grid(padx=7, pady=100)
FRAME.config(bg="black")



#Row 1
tk.Label(FRAME,
         font=DEFAULT_FONT,
         fg="red",
         width=16,
         text=SIDE_ONE
        ).grid(column=1, row=1)

tk.Label(FRAME, width=23).grid(column=2, row=4)

tk.Label(FRAME,
         font=DEFAULT_FONT,
         fg="red",
         width=16,
         text=SIDE_TWO
        ).grid(column=3, row=1)

#Row 2
tk.Label(FRAME,
         font=DEFAULT_FONT,
         fg="red",
         width=16,
         text=getstyle(SIDE_ONE)
        ).grid(column=1, row=2)

tk.Label(FRAME, width=20).grid(column=2, row=4)


tk.Label(FRAME,
         font=DEFAULT_FONT,
         fg="red",
         width=16,
         text=getstyle(SIDE_TWO)
        ).grid(column=3, row=2)

#Row 3
tk.Label(FRAME,
         font=DEFAULT_FONT,
         fg="red",
         width=16,
         text=gettemperature()
        ).grid(column=1, row=3)

tk.Label(FRAME, width=20).grid(column=2, row=4)

tk.Label(FRAME,
         font=DEFAULT_FONT,
         fg="red",
         width=16,
         text=gettemperature()
        ).grid(column=3, row=3)

#Row 4
tk.Label(FRAME,
         font=DEFAULT_FONT,
         fg="red",
         width=16,
         text=getabv(SIDE_TWO)
        ).grid(column=1, row=4)

tk.Label(FRAME, width=20).grid(column=2, row=4)

tk.Label(FRAME,
         font=DEFAULT_FONT,
         fg="red",
         width=16,
         text=getabv(SIDE_ONE)
        ).grid(column=3, row=4)

#Row 5
tk.Label(FRAME,
         font=DEFAULT_FONT,
         fg="red",
         width=16,
         text="Brew Date:"
        ).grid(column=1, row=5)

tk.Label(FRAME, width=20).grid(column=2, row=4)

tk.Label(FRAME,
         font=DEFAULT_FONT,
         fg="red",
         width=16,
         text="Brew Date:"
        ).grid(column=3, row=5)

#Row 6
tk.Label(FRAME,
         font=DEFAULT_FONT,
         fg="red",
         width=16,
         text=getbeerdate(SIDE_ONE)
        ).grid(column=1, row=6)

tk.Label(FRAME, width=20).grid(column=2, row=4)

tk.Label(FRAME,
         font=DEFAULT_FONT,
         fg="red",
         width=16,
         text=getbeerdate(SIDE_TWO)
        ).grid(column=3, row=6)

ROOT.mainloop()
