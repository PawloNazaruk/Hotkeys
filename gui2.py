from tkinter import *
import json


class MyApp:

    def __init__(self, parent, tags):
        self.myParent = parent


        self.myContainer1 = Frame(self.myParent)
        self.myContainer1.pack()

        self.button_New = Button(self.myContainer1, text="New Tag", bg="green")
        self.button_New.pack(side=LEFT)

        self.myContainer2 = Frame(self.myParent)
        self.myContainer2.pack(anchor=W)

        for tag in tags:
            print(tag['name'])
            self.myContainer_tag = Frame(self.myContainer2)
            self.myContainer_tag.pack()

            self.button_Update = Button(self.myContainer_tag, text="Update Tag", bg="yellow")
            self.button_Update.pack(side=LEFT)

            self.button_Delete = Button(self.myContainer_tag, text="Delete Tag", bg="red")
            self.button_Delete.pack(side=LEFT)

            self.label_Name = Label(self.myContainer_tag, text="Name: ", bg="cyan")
            self.label_Name.pack(side=LEFT)

            self.label_Name = Label(self.myContainer_tag, text=tag['name'], bg="white")
            self.label_Name.pack(side=LEFT)

            self.label_Switch_to = Label(self.myContainer_tag, text="Switch_to", bg="cyan")
            self.label_Switch_to.pack(side=LEFT)

            self.label_Switch_to = Label(self.myContainer_tag, text=tag['switch_to'], bg="white")
            self.label_Switch_to.pack(side=LEFT)



def get_tag_template(path = "template\\tags.json"):
    with open(path, "r") as file_ref:
        raw_data = json.load(file_ref)
        return raw_data



tags = get_tag_template()['tags']


root = Tk()
root.title("Hotkeys")
myapp = MyApp(root, tags)
root.mainloop()