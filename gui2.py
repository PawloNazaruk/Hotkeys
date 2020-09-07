from tkinter import *
from main import *
import json

# TODO: sortowanie przy zapisie/wczytaniu pliku

class MyApp:
    def __init__(self, root, tags):
        self.root = root
        self.tags = tags

        self.btn_new_tag = Button(self.root, text="New Tag", bg="green")
        self.btn_new_tag.bind("<Button-1>", lambda event: NewTagWindow(self.root, "New Tag"))
        self.btn_new_tag.pack(side=TOP, fill=X)
        self.frm_content = Frame(self.root, height=20, borderwidth=5, bg="black")
        self.frm_content.pack(fill=X)

        self.show_content()

    def show_content(self):
        try:
            self.frm_content_scroll.destroy()
        except AttributeError:
            pass
        finally:
            self.frm_content_scroll = ScrollableFrame(self.frm_content)

            for tag in self.tags:
                self.frm_tag = Frame(self.frm_content_scroll.scrollable_frame)
                self.frm_tag.pack(fill=X)

                self.btn_update_tag = Button(self.frm_tag, text="Update Tag", bg="yellow")
                self.btn_update_tag.bind("<Button-1>", lambda event:
                                            UpdateTagWindow(self.get_current_tag(event, ""), self.root, "Update Tag"))
                self.btn_update_tag.pack(side=LEFT)

                self.btn_delete_tag = Button(self.frm_tag, text="Delete Tag", bg="red")
                self.btn_delete_tag.bind("<Button-1>", lambda event:
                                            self.btn_delete_tag_click(event, self.get_current_tag(event, "2")))
                self.btn_delete_tag.pack(side=LEFT)

                self.lbl_name = Label(self.frm_tag, text="Name: ", bg="cyan")
                self.lbl_name.pack(side=LEFT)
                self.lbl_name_tag_value = Label(self.frm_tag, text=tag['name'], bg="white", width=18, anchor=W)
                self.lbl_name_tag_value.pack(side=LEFT)

                self.lbl_switch_to = Label(self.frm_tag, text="Switch_to", bg="cyan")
                self.lbl_switch_to.pack(side=LEFT)
                self.lbl_switch_to_tag_value = Label(self.frm_tag, text=tag['switch_to'], bg="white")
                self.lbl_switch_to_tag_value.pack(side=LEFT)

            self.frm_content_scroll.pack(fill=X)

    def get_current_tag(self, event, button_idx = ""):
        # TODO MAKE SIMPLER / regex??
        try:
            self.tag_idx = int(str(event.widget).replace(".!button" + button_idx, "")[46:]) - 1
        except ValueError:
            self.tag_idx = 0
        return self.tags[self.tag_idx]

    def btn_delete_tag_click(self, event, myDict):
        report_event(event)
        delete_tag(self.tags, myDict)
        AlertWindow(self.root, "Success", "Tag was deleted.")
        self.show_content()

# //////////////////////////////////////////////////////////

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

        self.frm_container_01 = Frame(self)
        self.frm_container_01.pack()

        self.button_Create = Button(self.frm_container_01, text="Update", bg="yellow")
        self.button_Create.bind("<Button-1>", self.buttonUpdateClick)
        self.button_Create.pack(side=LEFT)

        self.button_Cancel = Button(self.frm_container_01, text="Cancel", bg="red")
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
            self.destroy()
            return MyApp.show_content(myapp)

        AlertWindow(self, "Error", self.update_status)
        return

    def buttonCloseClick(self, event):
        report_event(event)
        self.destroy()
        MyApp.show_content()


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

        self.frm_container_01 = Frame(self)
        self.frm_container_01.pack()

        self.button_Create = Button(self.frm_container_01, text="Create", bg="green")
        self.button_Create.bind("<Button-1>", self.buttonCreateClick)
        self.button_Create.pack(side=LEFT)

        self.button_Cancel = Button(self.frm_container_01, text="Cancel", bg="red")
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