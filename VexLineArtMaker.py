from tkinter import *

current_x, current_y = 0,0


def locate_xy(event):
    global current_x, current_y
    current_x, current_y=event.x, event.y
    print(current_x,current_y)
    
def addLine(event):
    global current_x, current_y
    print(current_x,current_y,event.x,event.y)
    canvas.create_line((current_x,current_y,event.x,event.y))    
    
window = Tk()

window.title('Paint')
window.state( 'normal' )
window.config(bg='red')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

canvas=Canvas(window)
canvas.grid(row=0, column=0, sticky='nsew')

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)
#canvas.create_line(20,20,80,60)




window.mainloop()