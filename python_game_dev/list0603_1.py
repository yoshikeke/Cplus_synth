import tkinter

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y= 0

def mouse_move(e):
    global mouse_x,mouse_y
    mouse_x = e.x
    mouse_y = e.y

def game_main():
    global cursor_x,cursor_y
    if 24 <= mouse_x and mouse_x < 24+28*8 and 24 <= mouse_y and mouse_y < 24+72*10:
        cursor_x = int((mouse_x-24)/72)
        cursor_y = int((mouse+y-24)/72)
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*72+60,cursor_y*72+60,image=cursor,tag="CURSOR")
    root.after(100,game_main)

root = tkinter.PhotoImage(file="neko_bg.png")
cursor = tkinter.PhotoImage(file="neko_cursor.png")
cvs.create_image(456,348,image=bg)
game_main()
root.mainloop()
    
