from collections import namedtuple
from view.my_listbox import *
from clss.overwrite import *
from tkinter import messagebox
from tkinter import ttk

#import tkinter as tk



# TODO sliders shouldn't grow with bigger window or set window as static?


class MyApp:
    """
    Main Gui Class
    """
    def __init__(self, root, abbs, abbs_overwrite):
        self.root = root
        AbbsGroup = namedtuple("AbbGroup", [
            "abbs",
            "abbs_overwrite",
        ])
        # Keeps both lists objects under one var.
        self.abbs_group = AbbsGroup(abbs, abbs_overwrite)
        # Currently focused list object by a script.
        self.focused_abb = self.abbs_group[0]

        # self.display_menu_bar()  # Displays menu bar gui part. ATM turned off as it doesn't have big purpose.
        self.display_home()  # Displays main gui part.

    def display_home(self):
        """
        Displays main window of the gui app.
        Contains form on left side and listbox with control widgets on the right.
        """
        frm_background = tk.Frame(self.root, bg="green", height=800, width=600)
        frm_background.place(relheight=1, relwidth=1)
        self.display_form(frm_background)
        self.display_list_box_with_control_widgets(frm_background)

    def display_form(self, frm_background):
        """
        Setting up widgets.

        :param frm_background: total area which can be used by widgets
        """
        # Local frame of given area.
        self.frm_form = tk.Frame(frm_background)
        self.frm_form.place(relheight=1, relwidth=0.7)

        # Top "Name" section row.
        lbl_name = ttk.Label(self.frm_form, text="Name: ", anchor=tk.W, relief="groove")
        lbl_name.place(relx=0.00, rely=0.00, relheight=0.05, relwidth=0.08)
        self.ent_name = ttk.Entry(self.frm_form)
        self.ent_name.insert(0, "")
        self.ent_name.place(relx=0.08, rely=0.00, relheight=0.05, relwidth=0.92)

        # Middle "Text" section box.
        lbl_replace_to = ttk.Label(self.frm_form, text="Replace to: ", anchor=tk.W, relief="groove")
        lbl_replace_to.place(relx=0.00, rely=0.05, relheight=0.05, relwidth=0.12)
        self.txt_replace_to = tk.Text(self.frm_form)
        self.txt_replace_to.insert("1.0", "")
        self.txt_replace_to.place(relx=0.00, rely=0.10, relheight=0.85, relwidth=0.97)
        # Attaching slide_bar to the "text" widget.
        sb_replace_to = tk.Scrollbar(self.frm_form)
        sb_replace_to.place(relx=0.97, rely=0.10, relheight=0.85, relwidth=0.03)
        self.txt_replace_to.config(yscrollcommand=sb_replace_to.set)
        sb_replace_to.config(command=self.txt_replace_to.yview)

        if self.abbs_group.abbs.elements[0].name == "Help":
            help_info = self.abbs_group.abbs.elements[0].name
            self.ent_name.insert(0, help_info)
            help_info = self.abbs_group.abbs.elements[0].text
            self.txt_replace_to.insert("1.0", help_info)

        # Bottom "Buttons" row, which are created from other methods.

    def display_list_box_with_control_widgets(self, frm_background):
        """
        Setting up widgets.

        :param frm_background: total area which can be used by widgets
        """
        self.radio_value = tk.IntVar()  # Var to control focused_abb by radio buttons.
        # Local frame of given area.
        frm_list = tk.Frame(frm_background, bg="blue")
        frm_list.place(relx=0.7, relheight=1, relwidth=0.3)

        # Top "Radio buttons" row
        radio_btn_1 = tk.Radiobutton(frm_list, text="Tags", variable=self.radio_value, value=0,
                                     relief="groove", bd=3, tristatevalue="x", command=self.rb_status_switched)
        radio_btn_1.place(relx=0.0, rely=0.00, relheight=0.05, relwidth=0.5)
        radio_btn_2 = tk.Radiobutton(frm_list, text="Vars", variable=self.radio_value, value=1,
                                     relief="groove", bd=3, tristatevalue="x", command=self.rb_status_switched)
        radio_btn_2.place(relx=0.5, rely=0.00, relheight=0.05, relwidth=0.5)
        # Sets "abbs" as a default focused_abb list.
        radio_btn_2.select()
        if self.focused_abb == self.abbs_group.abbs:
            radio_btn_1.select()

        # Between Top row and list_box window, section for searching element name.
        ent_search_name = tk.Entry(frm_list)
        ent_search_name.bind("<Return>", self.process_search_button)
        ent_search_name.insert(0, 'Search for: "name" value')
        ent_search_name.place(rely=0.05, relheight=0.05, relwidth=1)

        # Middle "MyListbox" section.
        self.list_box = MyListbox(frm_list, selectmode="SINGLE", bg="white", activestyle="none")
        self.list_box.bind("<Return>", self.btn_show_item_clicked)
        self.list_box.place(rely=0.10, relheight=0.85, relwidth=0.93)
        self.list_box.insert_elements(self.focused_abb.elements)
        # Attaching slide_bar to the "list_box" widget.
        listbox_scrollbar = tk.Scrollbar(frm_list)
        listbox_scrollbar.place(relx=0.93, rely=0.10, relheight=0.85, relwidth=0.07)
        self.list_box.config(yscrollcommand=listbox_scrollbar.set)
        listbox_scrollbar.config(command=self.list_box.yview)

        # Bottom "CRUD buttons" row.
        btn_show_item = ttk.Button(frm_list, text="Show", command=self.btn_show_item_clicked)
        btn_show_item.place(relx=0.00, rely=0.95, relwidth=0.25, relheight=0.05)
        btn_new_item = ttk.Button(frm_list, text="New", command=self.btn_new_item_clicked)
        btn_new_item.place(relx=0.25, rely=0.95, relwidth=0.25, relheight=0.05)
        btn_update_item = ttk.Button(frm_list, text="Update", command=self.btn_update_item_clicked)
        btn_update_item.place(relx=0.50, rely=0.95, relwidth=0.25, relheight=0.05)
        btn_delete_item = ttk.Button(frm_list, text="Delete", command=self.process_delete_item)
        btn_delete_item.place(relx=0.75, rely=0.95, relwidth=0.25, relheight=0.05)

    def btn_show_item_clicked(self, evt=None):
        """
        Displays in form currently selected element in listbox.
        """
        abb = self.list_box.curselection_value()
        self.ent_name.delete(0, tk.END)
        self.ent_name.insert(0, abb.name)
        self.txt_replace_to.delete("1.0", tk.END)
        self.txt_replace_to.insert("1.0", abb.text)
        self.list_box.focus_set()

    def process_search_button(self, evt):
        """
        From given event takes written "name" value
        and searches if it is present in elements list.

        :param evt: Generated event.
        """
        w = evt.widget
        searched_name = w.get()
        for i, abb in enumerate(self.list_box.elements):
            if abb.name == searched_name:
                self.list_box.selection_set(i)
                self.list_box.focus_set()
                return None
        messagebox.showerror("Error", "Searched name cannot be found.")

    def display_menu_bar(self):
        """
        ATM not very useful, can be expanded in the future.
        Displays menu bar to the gui.
        """
        menu_bar = tk.Menu(self.root)
        menu_bar.add_command(label="Home", command=lambda: print("Home"))
        menu_bar.add_command(label="reg", command=lambda: print("reg"))
        self.root.config(menu=menu_bar)

    def rb_status_switched(self):
        """
        Switching radio button value causes to update focused_abb
        and display it elements in the list_box.
        """
        self.focused_abb = self.abbs_group[self.radio_value.get()]
        self.list_box.insert_elements(self.focused_abb.elements)

    def btn_new_item_clicked(self):
        """
        Clears form widgets from any text and adds button for
        further adding new item process. To prevent influence of the changes
        in focused_abb it stores its init value under own new_item_origin_group.
        """
        self.new_item_origin_group = self.focused_abb  # set origin list.
        self.ent_name.delete(0, tk.END)  # clears content from the "Name: "
        self.txt_replace_to.delete("1.0", tk.END)  # clears content from the "Replace to: "
        # Bottom "Buttons" row in form.
        btn_submit = ttk.Button(self.frm_form, text="Submit", command=self.process_new_item)
        btn_submit.place(relx=0.63, rely=0.95, relwidth=0.17, relheight=0.05)
        btn_cancel = ttk.Button(self.frm_form, text="Cancel", command=self.display_home)
        btn_cancel.place(relx=0.80, rely=0.95, relwidth=0.17, relheight=0.05)

    def process_new_item(self):
        """
        Validation of the given data if succeeded new element is added
        and list_box displays updated values.
        Depending on new_item_origin_group it performs process for abbs/abbs_overwrite.
        """
        name = self.ent_name.get()
        text = self.txt_replace_to.get("1.0", tk.END)[:-1]  # cut endl sign
        # Process of adding new item for abbs.
        if self.new_item_origin_group == self.abbs_group.abbs:
            try:
                self.abbs_group.abbs.add_element(name, text)
                self.list_box.insert_elements(self.abbs_group.abbs.elements)
                self.display_home()
                messagebox.showinfo("Success", "Given matching was created.")
            except BaseValidationError as err:
                messagebox.showerror("Error", err.msg)
        # Process of adding new item for abbs_overwrite.
        elif self.new_item_origin_group == self.abbs_group.abbs_overwrite:
            try:
                self.abbs_group.abbs_overwrite.add_element(name, text)
                # Invoking matching new abbreviation for Abb objects.
                for abb in self.abbs_group.abbs.elements:
                    abb.delete_abbreviation()
                self.abbs_group.abbs.set_all_abbreviation(self.abbs_group.abbs_overwrite.elements)
                self.list_box.insert_elements(self.abbs_group.abbs_overwrite.elements)
                self.display_home()
                messagebox.showinfo("Success", "Given matching was created.")
            except BaseValidationError as err:
                messagebox.showerror("Error", err.msg)

    def btn_update_item_clicked(self):
        """
        Fills form widgets with current item text and adds button for
        further update item process. To prevent influence of the changes
        in focused_abb it stores its init value under own new_item_origin_group.
        """
        self.new_item_origin_group = self.focused_abb  # set origin list
        self.ent_name.delete(0, tk.END)  # clears content from the "Name: "
        self.txt_replace_to.delete("1.0", tk.END)  # clears content from the "Replace to: "
        abb = self.list_box.curselection_value()

        self.ent_name.insert(0, abb.name)
        self.txt_replace_to.insert("1.0", abb.text)
        btn_submit = ttk.Button(self.frm_form, text="Submit", command=lambda: self.process_update_item(abb))
        btn_submit.place(relx=0.63, rely=0.95, relwidth=0.17, relheight=0.05)
        btn_cancel = ttk.Button(self.frm_form, text="Cancel", command=self.display_home)
        btn_cancel.place(relx=0.80, rely=0.95, relwidth=0.17, relheight=0.05)

    def process_update_item(self, abb):
        """
        Validation of the given data if succeeded new element is added
        and list_box displays updated values.
        Depending on new_item_origin_group it performs process for abbs/abbs_overwrite.

        :param abb: updated object
        """
        new_name = self.ent_name.get()
        new_text = self.txt_replace_to.get("1.0", tk.END)[:-1]  # cut endl sign
        # Process of adding new item for abbs.
        if self.new_item_origin_group == self.abbs_group.abbs:
            try:
                self.abbs_group.abbs.update_element(abb, new_name, new_text)
                self.list_box.insert_elements(self.abbs_group.abbs.elements)
                self.display_home()
                messagebox.showinfo("Success", "Matching was updated.")
            except BaseValidationError as err:
                messagebox.showerror("Error", err.msg)
        # Process of adding new item for abbs_overwrite.
        elif self.new_item_origin_group == self.abbs_group.abbs_overwrite:
            try:
                self.abbs_group.abbs_overwrite.update_element(abb, new_name, new_text)
                # Invoking matching new abbreviation for Abb objects.
                for abb in self.abbs_group.abbs.elements:
                    abb.delete_abbreviation()
                self.abbs_group.abbs.set_all_abbreviation(self.abbs_group.abbs_overwrite.elements)
                self.list_box.insert_elements(self.abbs_group.abbs_overwrite.elements)
                self.display_home()
                messagebox.showinfo("Success", "Given matching was created.")
            except BaseValidationError as err:
                messagebox.showerror("Error", err.msg)

    def process_delete_item(self):
        """
        Deletes currently selected item in list_box, and focused_abb list.
        """
        abb = self.list_box.curselection_value()

        if self.focused_abb == self.abbs_group.abbs:
            self.focused_abb.delete_element(abb)

        if self.focused_abb == self.abbs_group.abbs_overwrite:
            self.focused_abb.delete_element(abb)
            print("WOOLOLOLOLOL")
            for abb in self.abbs_group.abbs.elements:
                abb.delete_abbreviation()
            self.abbs_group.abbs.set_all_abbreviation(self.abbs_group.abbs_overwrite.elements)
        self.list_box.insert_elements(self.focused_abb.elements)


def report_event(event):
    """
    Print a description of an event, based on its attributes.
    """
    event_name = {"2": "KeyPress", "4": "ButtonPress"}
    print(f'Time: {event.time}')
    print(f'EventType={event.type}, {event_name[event.type]},\n \
        EventWidgetId={event.widget}, EventKeySymbol={event.keysym} \n')