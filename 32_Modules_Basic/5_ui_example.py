from tkinter import *
from tkinter import messagebox

def btn_click():
   #msg = messagebox.showinfo( "Hello Python", "Hello World")
    root.geometry("500x500")
    CharPhoto = PhotoImage(file = "c:\Python\gidigov.png")
    ChLabel = Label(root, image = CharPhoto,padx="100")
    ChLabel.place(x=125,y=150)
    ChLabel.img = CharPhoto
  
    
   # ChLabel.pack()


root = Tk()
root.geometry("500x100")

var = StringVar()
var.set("Wha'ts my favorite tv show?")
label = Label( root, textvariable=var, relief=FLAT ,text="Helvetica", font=("Helvetica", 16),fg="red") 
label.place(x=125,y=0)

B = Button(root, text = "click to find out!", command = btn_click)
B.place(x = 200,y = 50)

root.mainloop()