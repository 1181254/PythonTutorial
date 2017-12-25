from Tkinter import *

def action():
    print "this is awesome", txtName.get()


root = Tk()
root.title = "My GUI"

lblTitle = Label(root, text="Welcome")
# lblTitle.pack()
lblTitle.grid(row=0,column=0)

lblName = Label(root, text="Name")
#lblTitle.pack()
lblName.grid(row=1,column=0)

txtName = Entry(root)
# txtName.pack()
txtName.grid(row=1,column=1)

btn = Button(root, text="Submit", command=action)
# btn.pack()
btn.grid(row=2,column=0)

btnC = Button(root, text="Cancel", command=root.quit())
# btnC.pack()
btnC.grid(row=2,column=1)


root.mainloop()