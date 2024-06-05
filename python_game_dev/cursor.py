import tkinter

cursorX = 0
cursorY = 0
mouseX = 0
mouseY = 0

def mouse_move(e):
    global mouseX,mouseY
    mouseX = e.x
    mouseY = e.y

def game_main():
    global cursorX,cursorY
    cursorX = int(mouseX/72)
    cursorY = int(mouseY/72)
    cvs.delete("CURSOR")
    cvs.create_image(cursorX*72+60,cursorY*72+60,image=cursor,tag="CURSOR")
    root.after(100,game_main)

root = tkinter.Tk()
root.bind("<Motion>",mouse_move)
cvs = tkinter.Canvas(root,width=912,height=768)
cvs.pack()

cursor = tkinter.PhotoImage(file="neko_cursor.png")
game_main()
root.mainloop()
    
