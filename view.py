from tkinter import *
from main import *
import json
import re


class MyApp:
    def __init__(self, root, tags):
        self.root = root
        self.tags = tags

        self.display_screen_content()
        self.tag = ''
        self.new_tag = ''
        self.state = ''

    def display_screen_content(self):
        try:
            self.frm_tags_content.destroy()
        except AttributeError:
            pass
        finally:
            self.frm_tags_content = Frame(self.root, height=600, borderwidth=5, bg="black")
            self.frm_tags_content.pack(fill=X)
            self.btn_new_tag = Button(self.frm_tags_content, text="New Tag", bg="green")
            self.btn_new_tag.bind("<Button-1>", self.btn_new_tag_click)
            self.btn_new_tag.pack(side=TOP, fill=X)
            self.frm_content_scroll = ScrollableFrame(self.frm_tags_content)

            for tag in self.tags:
                self.frm_tag = Frame(self.frm_content_scroll.scrollable_frame)
                self.frm_tag.pack(fill=X)

                self.btn_update_tag = Button(self.frm_tag, text="Update Tag", bg="yellow")
                self.btn_update_tag.bind("<Button-1>", self.btn_update_tag_click)
                self.btn_update_tag.pack(side=LEFT)

                self.btn_delete_tag = Button(self.frm_tag, text="Delete Tag", bg="red")
                self.btn_delete_tag.bind("<Button-1>", self.btn_delete_tag_click)
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
            self.txt_to_text = Text(self.frm_tags_content)
            self.txt_to_text.pack(fill=X)

    def get_current_tag(self, event):
        report_event(event)
        current_tag_regex = re.compile("frame(\d*)\.!button")
        matched_object = current_tag_regex.findall(str(event.widget))
        tag_idx = matched_object[0]
        if tag_idx is "":
            tag_idx = 0
        else:
            tag_idx = int(tag_idx) - 1
        return self.tags[tag_idx]

    def btn_new_tag_click(self, event):
        self.display_screen_new_tag(event)

    def btn_update_tag_click(self, event):
        self.display_screen_update_tag(event)

    def btn_delete_tag_click(self, event):
        report_event(event)
        tag = self.get_current_tag(event)
        delete_tag(self.tags, tag)
        AlertWindow(self.root, "Success", "Tag was deleted.")
        self.display_screen_content()


    def display_screen_update_tag(self, event):
        try:
            self.frm_tags_content.destroy()
        except AttributeError:
            pass
        finally:
            self.tag = self.get_current_tag(event)

            self.frm_tags_content = Frame(self.root)
            self.frm_tags_content.pack(fill=X)

            self.lbl_name = Label(self.frm_tags_content, text="Name")
            self.lbl_name.pack()
            self.ent_name = Entry(self.frm_tags_content)
            self.ent_name.insert(0, self.tag["name"])
            self.ent_name.pack()

            self.lbl_switch_to = Label(self.frm_tags_content, text="Switch_to")
            self.lbl_switch_to.pack()
            self.txt_switch_to = Text(self.frm_tags_content)
            self.txt_switch_to.insert("1.0", self.tag["switch_to"])
            self.txt_switch_to.pack(fill=X)

            self.frm_buttons_line = Frame(self.frm_tags_content)
            self.frm_buttons_line.pack()

            self.btn_update = Button(self.frm_buttons_line, text="Update", bg="yellow")
            self.btn_update.bind("<Button-1>", self.btn_update_click)
            self.btn_update.pack(side=LEFT)

            self.btn_cancel = Button(self.frm_buttons_line, text="Cancel", bg="red")
            self.btn_cancel.bind("<Button-1>", self.btn_close_click)
            self.btn_cancel.pack(side=RIGHT)

    def btn_update_click(self, event):
        report_event(event)
        self.new_tag = dict()
        self.new_tag["name"] = self.ent_name.get()
        self.new_tag["switch_to"] = self.txt_switch_to.get("1.0", END)[:-1]

        update_status = update_tag(self.tags, self.tag, self.new_tag)
        if update_status == "Tag updated.":
            self.tag = self.new_tag
            AlertWindow(self.frm_tags_content, "Success", "Tag was updated.")
            self.frm_tags_content.destroy()
            return self.display_screen_content()

        AlertWindow(self.frm_tags_content, "Error", update_status)
        return

    def btn_close_click(self, event):
        report_event(event)
        self.frm_tags_content.destroy()
        self.display_screen_content()

    def display_screen_new_tag(self, event):
        try:
            self.frm_tags_content.destroy()
        except AttributeError:
            pass
        finally:
            self.frm_tags_content = Frame(self.root)
            self.frm_tags_content.pack(fill=X)

            self.lbl_name = Label(self.frm_tags_content, text="Name")
            self.lbl_name.pack()
            self.ent_name = Entry(self.frm_tags_content)
            self.ent_name.pack()

            self.lbl_switch_to = Label(self.frm_tags_content, text="Switch_to")
            self.lbl_switch_to.pack()
            self.txt_switch_to = Text(self.frm_tags_content)
            self.txt_switch_to.pack(fill=X)

            self.frm_buttons_line = Frame(self.frm_tags_content)
            self.frm_buttons_line.pack()

            self.btn_create = Button(self.frm_buttons_line, text="Create", bg="green")
            self.btn_create.bind("<Button-1>", self.btn_create_click)
            self.btn_create.pack(side=LEFT)

            self.btn_cancel = Button(self.frm_buttons_line, text="Cancel", bg="red")
            self.btn_cancel.bind("<Button-1>", self.btn_close_click)
            self.btn_cancel.pack(side=RIGHT)

    def btn_create_click(self, event):
        report_event(event)
        tag = dict(name="", switch_to="")
        tag["name"] = self.ent_name.get()
        tag["switch_to"] = self.txt_switch_to.get("1.0", END)[:-1]

        self.state = create_tag(self.tags, tag)
        if self.state == "Tag created.":
            AlertWindow(self.root, title="Success", text=self.state)
            self.frm_tags_content.destroy()
            return self.display_screen_content()

        AlertWindow(self.root, title="Error", text=self.state)


class AlertWindow(Toplevel):
    def __init__(self, master=None, title="Alert", text="temp"):
        super().__init__(master=master)
        self.title(title)
        self.geometry("250x150")

        self.lbl_alert = Label(self, text=text)
        self.lbl_alert.pack()


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


def get_template(path="template\\tags.json"):
    with open(path, "r") as file_ref:
        raw_data = json.load(file_ref)
        return raw_data
