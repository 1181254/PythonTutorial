from Tkinter import *
from tkFileDialog import askopenfilename

def createNewFile():
    print "New File Created"

def openAFile():
    name = askopenfilename()
    print "You selected: ",name

def exitFromApp():
    exit()

root = Tk()

menu = Menu(root)
root.config(menu=menu)

fMenu = Menu(menu)
menu.add_cascade(label="File", menu=fMenu)

fMenu.add_command(label="New", command=createNewFile)
fMenu.add_command(label="Open", command=openAFile)

fMenu.add_separator()

fMenu.add_command(label="Exit", command=exitFromApp)

hMenu = Menu(menu)
menu.add_cascade(label="Help", menu=hMenu)

hMenu.add_command(label="Find Action", command=createNewFile)
hMenu.add_command(label="Find", command=openAFile)

root.mainloop()