from tkinter import *
from tkinter import ttk
from datetime import *
while True:
    now = date.today()
    ifile = open(str(now), 'a+')

    root = Tk()
    root.title("Worker's Production")
    root.resizable(False,False)


    dateLabel = ttk.Label(root, text = "Date")
    dateEntry = ttk.Entry(root, width = 40)
    dateAutoBut = ttk.Button(root, text = "Auto")

    def dateAutoClick():
        dateEntry.insert(0, now)
    dateAutoBut.config(command = dateAutoClick)

    dateLabel.grid(row = 0, column = 0)
    dateEntry.grid(row = 0, column = 1)
    dateAutoBut.grid(row = 0, column = 2)

    nameLabel = ttk.Label(text = "Name")
    nameEntry = ttk.Entry(root, width = 40)
    nameLabel.grid(row = 1, column = 0)
    nameEntry.grid(row = 1, column = 1)

    designLabel = ttk.Label(text = "Design")
    designEntry = ttk.Entry(root, width = 40)
    designLabel.grid(row = 2, column = 0)
    designEntry.grid(row = 2, column = 1)

    colourLabel = ttk.Label(text = "Colour")
    colourEntry = ttk.Entry(root, width = 40)
    colourLabel.grid(row = 3, column = 0)
    colourEntry.grid(row = 3, column = 1)

    pickLabel = ttk.Label(text = "Pick")
    pickEntry = ttk.Entry(root, width = 40)
    pickLabel.grid(row = 4, column = 0)
    pickEntry.grid(row = 4, column = 1)

    startLabel = ttk.Label(root, text = "Starting piece number")
    startEntry = ttk.Entry(root, width = 40)
    startLabel.grid(row = 5, column = 0)
    startEntry.grid(row = 5, column = 1)

    endLabel = ttk.Label(root, text = "Ending piece number")
    endEntry = ttk.Entry(root, width = 40)
    endLabel.grid(row = 6, column = 0)
    endEntry.grid(row = 6, column = 1)

    pieceLabel = ttk.Label(root, text = "Total pieces")
    pieceEntry = ttk.Entry(root, width = 40)
    pieceAutoBut = ttk.Button(root, text = "Auto")


    def pieceAutoClick():
        pieceEntry.insert(0, (int(endEntry.get()) - int(startEntry.get())))
    pieceAutoBut.config(command = pieceAutoClick)
    pieceLabel.grid(row = 7, column = 0)
    pieceEntry.grid(row = 7, column = 1)
    pieceAutoBut.grid(row = 7, column = 2)

    # Code for Submit
    # Defining submit button
    submitBut = ttk.Button(root,text="Submit")
    submitBut.grid(row = 8, column = 0)


    # Definig submit button action
    def submitButClick():
        idate = dateEntry.get()
        iname = nameEntry.get()
        idesign = designEntry.get()
        icolour = colourEntry.get()
        ipick = pickEntry.get()
        istart = startEntry.get()
        iend = endEntry.get()
        ipiece = pieceEntry.get()
        ifile.write(idate + "," + iname + "," + idesign + "," + icolour + "," + ipick + "," + istart + "," + iend + "," + ipiece + "\n")
        ifile.close()
        startEntry.delete(0,END)
        endEntry.delete(0,END)
        nameEntry.delete(0,END)
        dateEntry.delete(0,END)
        designEntry.delete(0,END)
        pickEntry.delete(0,END)
        colourEntry.delete(0,END)
        pieceEntry.delete(0,END)
    # assigning action to button
    submitBut.config(command = submitButClick)
    # Code for Submit Ends


    # Code for Reset
    # Definig reset button
    resetBut = ttk.Button(root,text="Reset")
    resetBut.grid(row = 8, column = 1)





    #Defining reset buttom action
    def resetButClick():
        startEntry.delete(0,END)
        endEntry.delete(0,END)
        nameEntry.delete(0,END)
        dateEntry.delete(0,END)
        designEntry.delete(0,END)
        pickEntry.delete(0,END)
        colourEntry.dekete(0,END)
        pieceEntry.delete(0,END)
    # assigning action to reset button
    resetBut.config(command = resetButClick)
    # Code for Reset Ends








    # Loop to keep the GUI running
    root.mainloop()
    if root.destroy==1
