from tkinter import *

class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        self.button_OK = Button(self.myContainer1, text="OK!", bg="green")
        self.button_OK.pack(side=LEFT)
        self.button_OK.focus_force()
        self.button_OK.bind("<Button-1>", self.buttonOKClick)
        self.button_OK.bind("<Return>", self.buttonOKClick)

        self.button_Cancel = Button(self.myContainer1, text="Cancel Xd", bg="red")
        self.button_Cancel.pack(side=RIGHT)
        self.button_Cancel.bind("<Button-1>", self.buttonCancelClick)
        self.button_Cancel.bind("<Return>", self.buttonCancelClick)

    def buttonOKClick(self, event):
        if self.button_OK["background"] == "green":
            self.button_OK["background"] = "yellow"
        else:
            self.button_OK["bg"] = "green"

    def buttonCancelClick(self, event):
        self.myParent.destroy()

def report_event(event):
    """Print a description of an event, based on its attributes.
    """
    event_name = {"2": "KeyPress", "4": "ButtonPress"}
    print()






root = Tk()
myapp = MyApp(root)
root.mainloop()





"""class MyApp:
    def __init__(self, myParent):
        self.myContainer1 = Frame(myParent)
        self.myContainer1.pack()

        self.button1 = Button(self.myContainer1)
        self.button1["text"] = "Hello, World!"
        self.button1["background"] = "green"
        self.button1.pack(side=LEFT)

        self.button2 = Button(self.myContainer1)
        self.button2.configure(text="Off to join the circus!", background="blue")
        #self.button2.configure(width=42)
        self.button2.pack(side=LEFT)

        self.button3 = Button(self.myContainer1, text="Join me?", bg="cyan")
        self.button3.pack(side=LEFT)

        self.button3 = Button(self.myContainer1, text="Goodbye!", background="red")
        self.button3.pack(side=LEFT)

root = Tk()
myapp = MyApp(root)
root.mainloop()"""