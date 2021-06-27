import tkinter
import tkinter.messagebox
top=tkinter.Tk()


def hello():
    tkinter.messagebox.showinfo("Green","green button selected")
    
    

b1=tkinter.Button(top,text="Green",command=hello)


b1.pack()
b2.pack()

top.mainloop()