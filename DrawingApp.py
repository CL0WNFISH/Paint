from pickle import TRUE
from tkinter import ROUND, Button, Canvas, Label, PhotoImage, Tk
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
import tkinter
#Coded with hoe cakes -MF DOOM on repeat!!


root = Tk()
root.title("Drawing Board")
root.geometry("1050x570+150+50")
root.configure(bg="white")
root.resizable(False, False)

current_x = 0
current_y = 0
color =  "black"

def locate_xy(work):


    global current_x, current_y

    current_x = work.x
    current_y = work.y

def addLine(work):
    global current_x, current_y

    canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color, capstyle = ROUND)
    current_x, current_y = work.x, work.y

def show_color(new_color):
    global color


    color = new_color
def new_canvas():
    canvas.delete("all")
    display_palette()

image_icon = PhotoImage(file="c:/images/rock.png")
root.iconphoto(False,image_icon)

color_box = PhotoImage(file="c:/images/colorsection.png")
ColorBoxLabel = Label(root,image=color_box,bg="white").place(x=11.7,y=25)

eraser=PhotoImage(file="c:/images/eraser.png")
EraserButton = Button(root, image=eraser,bg="#ffffff", command=new_canvas, width=37,height=30,bd=0).place(x=30,y=400)


colors = Canvas(root,bg="#ffffff", width=37,height=300,bd=0)
colors.place(x=30,y=60)

def display_palette():
    id = colors.create_rectangle((10,10,30,30),fill="black")
    colors.tag_bind(id, "<Button-1>",lambda x: show_color("black"))

    id = colors.create_rectangle((10,40,30,60),fill="white")
    colors.tag_bind(id, "<Button-1>",lambda x: show_color("white"))

    id = colors.create_rectangle((10,70,30,90),fill="red")
    colors.tag_bind(id, "<Button-1>",lambda x: show_color("red"))

    id = colors.create_rectangle((10,100,30,120),fill="orange")
    colors.tag_bind(id, "<Button-1>",lambda x: show_color("orange"))

    id = colors.create_rectangle((10,130,30,150),fill="green")
    colors.tag_bind(id, "<Button-1>",lambda x: show_color("green"))

    id = colors.create_rectangle((10,160,30,180),fill="blue")
    colors.tag_bind(id, "<Button-1>",lambda x: show_color("blue"))

    id = colors.create_rectangle((10,190,30,210),fill="purple")
    colors.tag_bind(id, "<Button-1>",lambda x: show_color("purple"))

    id = colors.create_rectangle((10,220,30,240),fill="grey")
    colors.tag_bind(id, "<Button-1>",lambda x: show_color("grey"))

    id = colors.create_rectangle((10,220,30,240),fill="violet")
    colors.tag_bind(id, "<Button-1>",lambda x: show_color("violet"))

    id = colors.create_rectangle((10,250,30,270),fill="pink")
    colors.tag_bind(id, "<Button-1>",lambda x: show_color("pink"))

    id = colors.create_rectangle((10,280,30,300),fill="yellow")
    colors.tag_bind(id, "<Button-1>",lambda x: show_color("yellow"))

display_palette()

canvas = Canvas(root, width=930,height=480,background="white",cursor="hand2")
canvas.place(x=100,y=37.3)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', addLine)

current_value =tk.DoubleVar()

def get_current_value():
    return "{: .2f}".format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root,from_=0,to=10,orient="horizontal",command=slider_changed, variable=current_value)
slider.place(x=100,y=5)

value_label = ttk.Label(root, text=get_current_value(), font=("Roboto", 11))
value_label.place(x=5,y=5)



root.mainloop()
