import tkinter
root = tkinter.Tk()
root.title("first title")
root.geometry("800x600")
label = tkinter.Label(root,text='labels',font=("System",24))
label.place(x=200,y=100)
root.mainloop()
