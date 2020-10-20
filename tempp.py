from tkinter import *
from tkinter import messagebox

def onlbclick(evt):
    w=evt.widget
    index = int(w.curselection()[0])
    value=w.get(index)
    messagebox.showinfo("Listbox Select", f'You selected listitem {index}: {value}')



root =  Tk()
root.geometry("200x200")
root.title("List Box Test")
fr = Frame(root, width=200, height=200,bg="grey")
fr.pack()

lb=Listbox(fr,selectmode="BROWSE",bg="white")
lb.insert(1,"blah")
lb.insert(2,"blah blah")
lb.insert(3, "blah blah blah")
lb.insert(4, "blah blah blah blah")
lb.grid(row=1, rowspan=10, column=0,columnspan=5, sticky='W', padx=5, pady=5,ipadx=5, ipady=5)
lb.bind('<<ListboxSelect>>', onlbclick)

root.mainloop()