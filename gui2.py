from tkinter import *
from main import *
import json
import time

class MyApp:

    def __init__(self, parent, tags):
        self.myParent = parent

        self.myContainer1 = Frame(self.myParent, height=20, borderwidth=5, bg="black")
        self.myContainer1.pack(fill=X)

        self.button_NewTag = Button(self.myContainer1, text="New Tag", bg="green")
        self.button_NewTag.bind("<Button-1>", lambda event: NewTagWindow(self.myParent, "New Tag"))
        self.button_NewTag.pack(side=TOP, fill=X)

        self.myScrollable_frame = ScrollableFrame(self.myContainer1)

        for tag in tags:
            print(tag['name'])
            self.myContainer_tag = Frame(self.myScrollable_frame.scrollable_frame)
            self.myContainer_tag.pack(fill=X)

            self.button_UpdateTag = Button(self.myContainer_tag, text="Update Tag", bg="yellow")
            self.button_UpdateTag.bind("<Button-1>", lambda event: UpdateTagWindow(self.myParent, "Update Tag"))
            self.button_UpdateTag.pack(side=LEFT)

            self.button_DeleteTag = Button(self.myContainer_tag, text="Delete Tag", bg="red")
            self.button_DeleteTag.pack(side=LEFT)

            self.label_Name = Label(self.myContainer_tag, text="Name: ", bg="cyan")
            self.label_Name.pack(side=LEFT)

            self.label_Name = Label(self.myContainer_tag, text=tag['name'], bg="white", width=18, anchor=W)
            self.label_Name.pack(side=LEFT)

            self.label_Switch_to = Label(self.myContainer_tag, text="Switch_to", bg="cyan")
            self.label_Switch_to.pack(side=LEFT)

            self.label_Switch_to = Label(self.myContainer_tag, text=tag['switch_to'], bg="white")
            self.label_Switch_to.pack(side=LEFT)

        self.myScrollable_frame.pack(fill=X)
    """
    def buttonNewTagClick(self, event, master):
        report_event(event)
        self.myNewWindow = NewWindow(master)
    """
    def buttonUpdateTagClick(self):
        try:
            self.idx = int(str(event.widget).replace(".!button", "")[46:]) -1
        except ValueError:
            self.idx = 1 - 1
        self.myDict = tags[self.idx]
        #UpdateTagWindow(self.myParent, title="Update Tag Window")
        report_event(event)

class UpdateTagWindow(Toplevel):
    def __init__(self, master=None, title="Update Tag Window"):
        super().__init__(master)
        self.title(title)
        self.geometry("700x500")

class NewTagWindow(Toplevel):

    def __init__(self, master=None, title="New Tag Window"):
        super().__init__(master=master)
        self.title(title)
        self.geometry("700x500")

        self.label_Name = Label(self, text="Name")
        self.label_Name.pack()

        self.entry_Name = Entry(self)
        self.entry_Name.pack()

        self.label_Switch_to = Label(self, text="Switch_to")
        self.label_Switch_to.pack()

        self.text_Switch_to = Text(self)
        self.text_Switch_to.pack(fill=X)

        self.myContainer1 = Frame(self)
        self.myContainer1.pack()

        self.button_Create = Button(self.myContainer1, text="Create", bg="green")
        self.button_Create.bind("<Button>", self.buttonCreateClick)
        self.button_Create.pack(side=LEFT)

        self.button_Cancel = Button(self.myContainer1, text="Cancel", bg="red")
        self.button_Cancel.bind("<Button-1>", self.buttonCancelClick)
        self.button_Cancel.pack(side=RIGHT)


    def buttonCreateClick(self, event):
        report_event(event)
        self.myDict = dict(name="", switch_to="")

        self.myDict["name"] = self.entry_Name.get()
        self.myDict["switch_to"] = self.text_Switch_to.get("1.0", END)[:-1]

        self.state = create_tag(tags, self.myDict)
        AlertWindow(self, title="Alert", text=self.state)


    def buttonCancelClick(self, event):
        report_event(event)
        self.destroy()


class AlertWindow(Toplevel):

    def __init__(self, master=None, title="Alert", text="temp"):
        super().__init__(master=master)
        self.title(title)
        self.geometry("200x200")

        self.label_Alert = Label(self, text=text)
        self.label_Alert.pack()



class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self)
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


def report_event(event):
    """Print a description of an event, based on its attributes.
    """
    event_name = {"2": "KeyPress", "4": "ButtonPress"}
    print(f'Time: {event.time}')
    print(f'EventType={event.type}, {event_name[event.type]},\n \
        EventWidgetId={event.widget}, EventKeySymbol={event.keysym} \n')


def get_tag_template(path = "template\\tags.json"):
    with open(path, "r") as file_ref:
        raw_data = json.load(file_ref)
        return raw_data



tags = get_tag_template()['tags']

asd = dict(name="123", switch_to="234")
create_tag(tags, asd)

root = Tk()
root.geometry("800x300")
root.title("Hotkeys")
myapp = MyApp(root, tags)
root.mainloop()