from tkinter import *
from main import *
import json
from pprint import pprint

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
            self.button_UpdateTag.bind("<Button-1>", \
                                       lambda event: UpdateTagWindow(self.getCurrentTagDict(event, tags), self.myParent, "Update Tag"))
            self.button_UpdateTag.pack(side=LEFT)



            self.button_DeleteTag = Button(self.myContainer_tag, text="Delete Tag", bg="red")
            self.button_DeleteTag.bind("<Button-1>", lambda event: self.buttonDeleteClick(event, tags, self.getCurrentTagDict(event, tags, "2")))

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



    def getCurrentTagDict(self, event, tags, button_idx = ""):
        try:
            self.idx = int(str(event.widget).replace(".!button" + button_idx, "")[46:]) - 1
        except ValueError:
            self.idx = 1 - 1
        self.myDict = tags[self.idx]
        return self.myDict

    def buttonDeleteClick(self, event, tags, myDict):
        report_event(event)
        delete_tag(tags, myDict)
        AlertWindow(self.myParent, "Success", "Tag was deleted.")



class UpdateTagWindow(Toplevel):
    def __init__(self, myDict, master=None, title="Update Tag Window"):
        super().__init__(master)
        self.title(title)
        self.geometry("700x500")
        self.myDict = myDict

        self.label_Name = Label(self, text="Name")
        self.label_Name.pack()

        self.entry_Name = Entry(self)
        self.entry_Name.insert(0, self.myDict["name"])
        self.entry_Name.pack()

        self.label_Switch_to = Label(self, text="Switch_to")
        self.label_Switch_to.pack()

        self.text_Switch_to = Text(self)
        self.text_Switch_to.insert("1.0", self.myDict["switch_to"])
        self.text_Switch_to.pack(fill=X)

        self.myContainer1 = Frame(self)
        self.myContainer1.pack()

        self.button_Create = Button(self.myContainer1, text="Update", bg="yellow")
        self.button_Create.bind("<Button-1>", self.buttonUpdateClick)
        self.button_Create.pack(side=LEFT)

        self.button_Cancel = Button(self.myContainer1, text="Cancel", bg="red")
        self.button_Cancel.bind("<Button-1>", self.buttonCloseClick)
        self.button_Cancel.pack(side=RIGHT)

    def buttonUpdateClick(self, event):
        report_event(event)
        self.newDict = dict(name="", switch_to="")
        self.newDict["name"] = self.entry_Name.get()
        self.newDict["switch_to"] = self.text_Switch_to.get("1.0", END)[:-1]

        self.update_status = update_tag(tags, self.myDict, self.newDict)
        if self.update_status == "Tag updated.":
            self.myDict = self.newDict
            AlertWindow(self, "Success", "Tag was updated.")
            return

        AlertWindow(self, "Error", self.update_status)
        return

    def buttonCloseClick(self, event):
        report_event(event)
        self.destroy()


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
        self.button_Create.bind("<Button-1>", self.buttonCreateClick)
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
        AlertWindow(self, title="Error", text=self.state)

    def buttonCancelClick(self, event):
        report_event(event)
        self.destroy()


class AlertWindow(Toplevel):

    def __init__(self, master=None, title="Alert", text="temp"):
        super().__init__(master=master)
        self.title(title)
        self.geometry("250x150")

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

root = Tk()
root.geometry("800x300")
root.title("Hotkeys")
myapp = MyApp(root, tags)
root.mainloop()