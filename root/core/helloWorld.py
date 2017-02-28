#Austin Dillinger 02/16/2017 

from tkinter import  *
from tkinter import ttk

root = Tk()
root.title("Beer!")

mainframe = ttk.Frame(root,padding="5 5 5 5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

headerSideOne = StringVar()
headerSideTwo = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable="beer")
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=headerSideOne).grid(column=2, row=2, sticky=(W, E))
#ttk.Button(mainframe, text="Calculate", command=exit).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="kegPieceOne").grid(column=1, row=1, sticky=N)
ttk.Label(mainframe, text="hopProfileOne").grid(column=2, row=1, sticky=N)
ttk.Label(mainframe, text="hopProfileTwo").grid(column=3, row=1, sticky=N)
ttk.Label(mainframe, text="kegPieceOne").grid(column=4, row=1, sticky=N)

ttk.Label(mainframe, text="kegPieceTwoWTemp").grid(column=1, row=2, sticky=N)
ttk.Label(mainframe, text="ABV").grid(column=2, row=2, sticky=N)
ttk.Label(mainframe, text="ABV").grid(column=3, row=2, sticky=N)
ttk.Label(mainframe, text="kegPieceTwoWTemp").grid(column=4, row=2, sticky=N)

ttk.Label(mainframe, text="kegPieceThree").grid(column=1, row=3, sticky=N)
ttk.Label(mainframe, text="beerType").grid(column=2, row=3, sticky=N)
ttk.Label(mainframe, text="beerType").grid(column=3, row=3, sticky=N)
ttk.Label(mainframe, text="kegPieceThree").grid(column=4, row=3, sticky=N)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', exit)

#ttk.Button(root, text="Hello World").grid()
root.mainloop()