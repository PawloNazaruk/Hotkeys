from tkinter import *

class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        self.button_OK = Button(self.myContainer1, command=self.buttonOKClick2, text="OK!", bg="green")
        self.button_OK.pack(side=LEFT)
        self.button_OK.focus_force()
        #self.button_OK.bind("<Button-1>", self.buttonOKClick)
        #self.button_OK.bind("<Return>", self.buttonOKClick)

        self.button_Cancel = Button(self.myContainer1, text="Cancel Xd", bg="red")
        self.button_Cancel.pack(side=RIGHT)
        self.button_Cancel.bind("<Button-1>", self.buttonCancelClick)
        self.button_Cancel.bind("<Return>", self.buttonCancelClick)


    def buttonOKClick(self, event):
        report_event(event)
        if self.button_OK["background"] == "green":
            self.button_OK["background"] = "yellow"
        else:
            self.button_OK["bg"] = "green"

    def buttonOKClick2(self):
        #report_event(event)
        if self.button_OK["background"] == "green":
            self.button_OK["background"] = "yellow"
        else:
            self.button_OK["bg"] = "green"

    def buttonCancelClick(self, event):
        report_event(event)
        self.myParent.destroy()


def report_event(event):
    """Print a description of an event, based on its attributes.
    """
    event_name = {"2": "KeyPress", "4": "ButtonPress"}
    print(f'Time: {event.time}')
    print(f'EventType={event.type}, {event_name[event.type]},\n \
        EventWidgetId={event.widget}, EventKeySymbol={event.keysym} \n')


root = Tk()
myapp = MyApp(root)
root.mainloop()