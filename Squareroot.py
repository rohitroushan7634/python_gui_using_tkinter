from tkinter import *
win = Tk()
win.title("SquareRoot")
win.maxsize(width=600,height=500)
win.minsize(width=600,height=500)
#function
def func():
    var.get()

#label
lbl = Label(win,text="Enter Number",bg="red",fg="white")
lbl.place(x=100,y=100)

lbl = Label(win,text="Number which is entered by you",bg="red",fg="white")
lbl.place(x=100,y=150)
lbl = Label(win,text="Square root of that number",bg="red",fg="white")
lbl.place(x=100,y=180)

#entry
var = StringVar()
ent = Entry(win,bg="red",fg='white',bd=5,textvariable=var)
ent.place(x=200,y=100)

#button
btn = Button(win,text="Find SquareRoot",bg='green',command=func)
btn.place(x=100,y=2500)





win.mainloop()