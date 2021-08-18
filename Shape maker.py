from tkinter import*
from tkinter import ttk

root=Tk()
root.title("Shapes")
root.geometry("600x600")

choose_colour=Label(root,text="Choose color")
startx=Label(root,text="startx")
starty=Label(root,text="starty")
endx=Label(root,text="endx")
endy=Label(root,text="endy")

oldx=startx
oldy=starty
newx=endx
newy=endy
coordinates_value=[10,50,100,200,300,400,500,600,800,900]
fillcolour=["blue","red","white","green","pink","purple","orange","yellow"]
colour_dropdown=ttk.Combobox(root,state="readonly",value=fillcolour,width=10)
colour_dropdown.place(relx=0.9,rely=0.9,anchor=CENTER)
d1=ttk.Combobox(root,state="readonly",value=fillcolour,width=10)
canvas=Canvas(root,width=800,height=450,bg="white",highlightbackground="black")
startX=ttk.Combobox(root,state="readonely",value=coordinates_value,width=10)
startX.place(relx=0.1,rely=0.8,anchor=CENTER)
startY=ttk.Combobox(root,state="readonely",value=coordinates_value,width=10)
startY.place(relx=0.4,rely=0.8,anchor=CENTER)
canvas.pack()
endX=ttk.Combobox(root,state="readonely",value=coordinates_value,width=10)
endX.place(relx=0.6,rely=0.8,anchor=CENTER)
endY=ttk.Combobox(root,state="readonely",value=coordinates_value,width=10)
endY.place(relx=0.9,rely=0.8,anchor=CENTER)

def circle(event):
    global oldx
    global oldy
    global newx
    global newy
    startX.get()
    startY.get()
    endX.get()
    endY.get()
    if keypress=='c':
        draw_circle=canvas.create_oval(oldx,oldy,newx,newy,fill=fillcolour)
def rectangle(event):
    global oldx
    global oldy
    global newx
    global newy
    startX.get()
    startY.get()
    endX.get()
    endY.get()
    if keypress=='r':
        draw_rectangle=canvas.create_rectangle(oldx,oldy,newx,newy,fill=fillcolour)

def draw(keypress,oldx,oldy,newx,newy):
    fillcolour.get()
    root.bind("<c>",circle)
    root.bind("<r>",rectangle)
    
    
    

root.mainloop()