from Tkinter import *

def onClick():
    print "This is Awesome", entryName.get()

root = Tk()
root.title = "Registration"

lblTitle = Label(root,text="Welcome User")
#lblTitle.pack()
lblTitle.grid(row=0,column=0)

lblName = Label(root,text="Enter Your Name")
#lblTitle.pack()
lblName.grid(row=0,column=0)

entryName = Entry(root)
# entryName.pack()
entryName.grid(row=1,column=0)

btnSubmit = Button(root,text="Submit", command=onClick)
# btnSubmit.pack()
btnSubmit.grid(row=2,column=0)

root.mainloop()