from Tkinter import *
import tkMessageBox
import tkColorChooser
import tkFileDialog

#This is the main file that executes the QC Tool


#UI
root = Tk()
mainframe = Frame(root, bg = "black")
mainframe.pack(expand = True, fill = BOTH)
topframe = Frame(mainframe, bg = "black")
bottomframe = Frame(mainframe, bg = "black")
titleframe = Frame(topframe, bg = "black", padx = 10, pady = 10)
mainlabel = Label(titleframe, text = "Better Work Flow", fg = "orange", bg = 'black', font = ('Helvetica', 24))
sublabel = Label(titleframe, text = "- QC Enhancement -", fg = "orange", bg = 'black', font = ('Helvetica', 16))
uwffilechecklabel = Label(bottomframe, text = "UWF FILE CHECK" ,fg = 'white', bg = "black", font = ('Helvectica', 14))
uwffilecheckbox = Label(bottomframe, text = "ONLINE", fg = "white", bg = "blue", font = ('Helvectica', 14))
topframe.pack(side = TOP, anchor = NW)
titleframe.pack(side = TOP, anchor = W)
mainlabel.pack()
sublabel.pack()
bottomframe.pack(anchor = NW)
uwffilechecklabel.pack(side = LEFT, anchor = NW)
uwffilecheckbox.pack(side = LEFT, anchor = NW)
root.mainloop()
