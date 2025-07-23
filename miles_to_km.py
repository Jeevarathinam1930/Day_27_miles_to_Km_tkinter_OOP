from tkinter import *
def calculate():
    miles_input=entry.get()
    km=int(miles_input)*1.6
    label_change["text"]=km
window=Tk()
entry=Entry()
entry.grid(row=0,column=1)
label1=Label(text="Miles")
label1.grid(row=0,column=2)
label2=Label(text="is equal to ")
label2.grid(row=1,column=0)
label_change=Label(text="0")
label_change.grid(row=1,column=1)
label3=Label(text="Km")
label3.grid(row=1,column=2)
button=Button(text="Calculate",command= calculate)
button.grid(row=2,column=1)
window.mainloop()