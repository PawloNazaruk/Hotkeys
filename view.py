from tkinter import *
from main import *
from tags import *
from vars import *
from CRUD import *
from collections import namedtuple
import re


class MyApp:
    def __init__(self, root, tags, variables):
        self.root = root
        self.tags = tags
        self.variables = variables
        self.Item = namedtuple("Item", "type list path name switch_to")
        self.tag_item = self.Item("tag", self.tags, PATH_TAGS, "Tag name:", "Switch to:")
        self.var_item = self.Item("var", self.variables, PATH_VARS, "Variable name:", "Switch to:")
        self.my_active_tuple = ()
        self.display_home()

    def btn_clicked_display_create_tag(self, event):
        self.my_active_tuple = self.Item(*self.tag_item)
        self.display_create_item(event)

    def btn_clicked_display_tags(self, event):
        self.my_active_tuple = self.Item(*self.tag_item)
        self.display_content(event)

    def btn_clicked_display_create_var(self, event):
        self.my_active_tuple = self.Item(*self.var_item)
        self.display_create_item(event)

    def btn_clicked_display_vars(self, event):
        self.my_active_tuple = self.Item(*self.var_item)
        self.display_content(event)

    def display_menubar(self):
        menubar = Menu(self.root)
        menubar.add_command(label="Home", command=lambda: self.display_home())

        tags = Menu(menubar, tearoff=False)
        tags.add_command(label="New Tag", command=lambda: self.display_create_item("tags"))
        tags.add_command(label="Show Tags", command=lambda: self.display_content)
        menubar.add_cascade(label="Tags", menu=tags)

        variables = Menu(menubar, tearoff=False)
        variables.add_command(label="New Var", command=lambda: self.display_create_item("vars"))
        variables.add_command(label="Show Vars", command=lambda: self.display_content)
        menubar.add_cascade(label="Vars", menu=variables)

        self.root.config(menu=menubar)

    def display_home(self):
        self.display_menubar()
        try:
            self.frm_background.destroy()
        except AttributeError:
            pass
        finally:
            self.frm_background = Frame(self.root)

            lbl_test_yours_hotkey = Label(self.frm_background, text="Test your hotkey:")
            lbl_test_yours_hotkey.pack()
            txt_test_yours_hotkey = Text(self.frm_background)
            txt_test_yours_hotkey.pack()

            frm_line_tag = Frame(self.frm_background)
            btn_show_create_tag = Button(frm_line_tag, text="Create Tag")
            btn_show_create_tag.bind("<Button-1>", self.btn_clicked_display_create_tag)
            btn_show_create_tag.pack(fill=X)
            btn_show_tags = Button(frm_line_tag, text="Show Tags")
            btn_show_tags.bind("<Button-1>", self.btn_clicked_display_tags)
            btn_show_tags.pack(fill=X)
            frm_line_tag.pack(fill=X)

            frm_line_vars = Frame(self.frm_background)
            btn_show_create_var = Button(frm_line_vars, text="Create Var")
            btn_show_create_var.bind("<Button-1>", self.btn_clicked_display_create_var)
            btn_show_create_var.pack(fill=X)
            btn_show_vars = Button(frm_line_vars, text="Show Vars")
            btn_show_vars.bind("<Button-1>", self.btn_clicked_display_vars)
            btn_show_vars.pack(fill=X)
            frm_line_vars.pack(fill=X)

            self.frm_background.pack()

    def display_content(self, event):
        self. display_menubar()

        try:
            self.frm_background.destroy()
        except AttributeError:
            pass
        finally:
            self.frm_background = Frame(self.root)
            self.frm_background.pack(fill=X)
            frm_background_scrollable = ScrollableFrame(self.frm_background)

            for my_dict in self.my_active_tuple.list:
                frm_data_row = Frame(frm_background_scrollable.scrollable_frame)
                frm_data_row.pack(fill=X)

                btn_show_update_item = Button(frm_data_row, text="Update "+self.my_active_tuple.type, bg="yellow")
                btn_show_update_item.bind("<Button-1>", self.display_update_item)
                btn_show_update_item.pack(side=LEFT)

                btn_perform_delete_item = Button(frm_data_row, text="Delete "+self.my_active_tuple.type, bg="red")
                btn_perform_delete_item.bind("<Button-1>", self.perform_delete_item)
                btn_perform_delete_item.pack(side=LEFT)

                lbl_item_name = Label(frm_data_row, text="Name: ", bg="cyan")
                lbl_item_name.pack(side=LEFT)
                lbl_item_name_value = Label(frm_data_row, text=my_dict["name"], bg="white", width=18, anchor=W)
                lbl_item_name_value.pack(side=LEFT)

                lbl_item_switch_to = Label(frm_data_row, text="Switch to: ", bg="cyan")
                lbl_item_switch_to.pack(side=LEFT)
                lbl_item_switch_to_value = Label(frm_data_row, text=my_dict["switch_to"], bg="white")
                lbl_item_switch_to_value.pack(side=LEFT)
            frm_background_scrollable.pack(fill=X)

    def display_create_item(self, event):
        self.display_menubar()

        try:
            self.frm_background.destroy()
        except AttributeError:
            pass
        finally:
            self.frm_background = Frame(self.root)

            frm_line_header = Frame(self.frm_background)
            lbl_item_name = Label(frm_line_header, text=self.my_active_tuple.name)
            lbl_item_name.pack()
            self.ent_item_name_value = Entry(frm_line_header)
            self.ent_item_name_value.pack(fill=X)

            lbl_item_switch_to_value = Label(frm_line_header, text=self.my_active_tuple.switch_to)
            lbl_item_switch_to_value.pack()
            self.txt_item_switch_to_value = Text(frm_line_header)
            self.txt_item_switch_to_value.pack(fill=X)
            frm_line_header.pack()

            frm_line_buttons = Frame(self.frm_background)
            btn_perform_create_item = Button(frm_line_buttons, text="Create", bg="green")
            btn_perform_create_item.bind("<Button-1>", self.perform_create_item)
            btn_perform_create_item.pack(fill=X)
            btn_perform_exit = Button(frm_line_buttons, text="Cancel", bg="red")
            btn_perform_exit.bind("<Button-1>", self.perform_exit)
            btn_perform_exit.pack(fill=X)
            frm_line_buttons.pack(fill=X)

            self.frm_background.pack()

    def display_update_item(self, event):
        self.display_menubar()

        try:
            self.frm_background.destroy()
        except AttributeError:
            pass
        finally:
            self.my_item = self.get_current_item_from_content(event)

            self.frm_background = Frame(self.root)

            frm_line_header = Frame(self.frm_background)
            lbl_item_name = Label(frm_line_header, text=self.my_active_tuple.name)
            lbl_item_name.pack()
            self.ent_item_name_value = Entry(frm_line_header)
            self.ent_item_name_value.insert(0, self.my_item["name"])
            self.ent_item_name_value.pack(fill=X)

            lbl_item_switch_to_value = Label(frm_line_header, text=self.my_active_tuple.switch_to)
            lbl_item_switch_to_value.pack()
            self.txt_item_switch_to_value = Text(frm_line_header)
            self.txt_item_switch_to_value.insert("1.0", self.my_item["switch_to"])
            self.txt_item_switch_to_value.pack(fill=X)
            frm_line_header.pack()

            frm_line_buttons = Frame(self.frm_background)
            btn_perform_create_item = Button(frm_line_buttons, text="Update", bg="green")
            btn_perform_create_item.bind("<Button-1>", self.perform_create_item)
            btn_perform_create_item.pack(fill=X)

            btn_perform_exit = Button(frm_line_buttons, text="Cancel", bg="red")
            btn_perform_exit.bind("<Button-1>", self.display_content)
            btn_perform_exit.pack(fill=X)
            frm_line_buttons.pack(fill=X)

            self.frm_background.pack()

    def perform_create_item(self, event):
        my_dict = dict(name="", switch_to="")
        my_dict["name"] = self.ent_item_name_value.get()
        my_dict["switch_to"] = self.txt_item_switch_to_value.get("1.0", END)[:-1]

        try:
            if "tag" in self.my_active_tuple.type:
                add_tag(self.tags, self.variables, my_dict, self.my_active_tuple.path)
            elif "var" in self.my_active_tuple.type:
                add_var(self.variables, my_dict, self.my_active_tuple.path)
        except FillBothEntries as err:
            AlertWindow(self.root, title="Error", text=err.msg)
        except FillName as err:
            AlertWindow(self.root, title="Error", text=err.msg)
        except FillSwitchTo as err:
            AlertWindow(self.root, title="Error", text=err.msg)
        except DictWithNameAlreadyUsed as err:
            log = "Cannot add: Name: " + str(my_dict["name"]) + " - " + str(err.msg)
            AlertWindow(self.root, title="Error", text=log)
        else:
            AlertWindow(self.root, title="Success", text="Created.")
            self.display_home()

    def perform_update_item(self, event):
        my_dict = dict(name="", switch_to="")
        my_dict["name"] = self.ent_item_name_value.get()
        my_dict["switch_to"] = self.txt_item_switch_to_value.get("1.0", END)[:-1]

        try:
            if "tag" in self.my_active_tuple.type:
                update_tag(self.tags, self.variables, self.my_item, my_dict, self.my_active_tuple.path)
            elif "var" in self.my_active_tuple.type:
                update_var(self.variables, self.my_item, my_dict, self.my_active_tuple.path)
        except FillBothEntries as err:
            AlertWindow(self.root, title="Error", text=err.msg)
        except FillName as err:
            AlertWindow(self.root, title="Error", text=err.msg)
        except FillSwitchTo as err:
            AlertWindow(self.root, title="Error", text=err.msg)
        except DictWithNameAlreadyUsed as err:
            log = "Cannot add: Name: " + str(my_dict["name"]) + " - " + str(err.msg)
            AlertWindow(self.root, title="Error", text=log)
        else:
            AlertWindow(self.root, title="Success", text="Updated.")
            self.display_home()

    def perform_delete_item(self, event):
        report_event(event)
        item_to_delete = self.get_current_item_from_content(event)
        try:
            delete_tag(self.my_active_tuple.list, item_to_delete, self.my_active_tuple.path)
        except DictDoesntExistInList as err:
            AlertWindow(self.root, "Error", "There is no such " + self.my_active_tuple.type)
        else:
            AlertWindow(self.root, "Success", "Tag was deleted.")
            self.display_home()

    def perform_exit(self, event):
        self.display_home()

    def get_current_item_from_content(self, event):
        report_event(event)
        item_regex = re.compile("frame(\d*)\.!button")
        matched_object = item_regex.findall(str(event.widget))
        item_idx = matched_object[0]
        if item_idx is "":
            item_idx = 0
        else:
            item_idx = int(item_idx) - 1
        return self.my_active_tuple.list[item_idx]


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


