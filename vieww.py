import tkinter as tk
from tags import *
from pprint import pprint

# TODO sliders shouldn't grow with bigger window


class MyApp:
    abbreviation = []
    abbreviation_overwrite = []

    def __init__(self, root, abbreviation, abbreviation_overwrite):
        self.root = root
        self.abbreviation = abbreviation
        self.abbreviation_overwrite = abbreviation_overwrite
        self.lsts = [self.abbreviation, self.abbreviation_overwrite]
        self.current_abb = self.lsts[0]

        self.lst_temp = [x for x in range(101)]

        self.display_menubar()
        self.display_home()

        self.current_list = tk.IntVar()

    def display_menubar(self):
        """ Displays menu bar to the gui.
        :return:
        """
        menu_bar = tk.Menu(self.root)
        menu_bar.add_command(label="Home", command=lambda: print("Home"))
        menu_bar.add_command(label="reg", command=lambda: print("reg"))
        self.root.config(menu=menu_bar)

    def display_home(self):
        """ Displays main window of the gui app.
        Contains form on left side and listbox on right.
        :return:
        """
        self.radio_value = tk.IntVar()
        frm_background = tk.Frame(self.root, bg="green", height=800, width=600)
        frm_background.place(relheight=1, relwidth=1)

        # lewa strona widoku
        frm_form = tk.Frame(frm_background)
        frm_form.place(relheight=1, relwidth=0.7)
        # górny wiersz
        lbl_name = tk.Label(frm_form, text="Name: ", anchor=tk.W, bd=2, relief="groove")
        lbl_name.place(relx=0.00, rely=0.00, relheight=0.05, relwidth=0.08)
        ent_name = tk.Entry(frm_form)
        ent_name.insert(0, "Name Placeholder...")
        ent_name.place(relx=0.08, rely=0.00, relheight=0.05, relwidth=0.92)
        # srodkowe okno tekstowe
        lbl_switch_to = tk.Label(frm_form, text="Switch to: ", anchor=tk.W, bd=2, relief="groove")
        lbl_switch_to.place(relx=0.00, rely=0.05, relheight=0.05, relwidth=0.11)
        txt_switch_to = tk.Text(frm_form)
        txt_switch_to.insert("1.0", "Text Placeholder..."*200)
        txt_switch_to.place(relx=0.00, rely=0.10, relheight=0.85, relwidth=0.97)
        # dodanie scrollbara do pola tekstowego
        sb_switch_to = tk.Scrollbar(frm_form)
        sb_switch_to.place(relx=0.97, rely=0.10, relheight=0.85, relwidth=0.03)
        txt_switch_to.config(yscrollcommand=sb_switch_to.set)
        sb_switch_to.config(command=txt_switch_to.yview)
        # przycisk do zatwierdzenia wpisow
        btn_submit = tk.Button(frm_form, text="Submit", bd=3)
        btn_submit.place(relx=0.8, rely=0.95, relwidth=0.17, relheight=0.05)

        # prawa strona widoku
        frm_list = tk.Frame(frm_background, bg="blue")
        frm_list.place(relx=0.7, relheight=1, relwidth=0.3)
        # zaznaczenie wyswietlanai aktualnej listy
        radio_btn_1 = tk.Radiobutton(frm_list, text="Tags", variable=self.radio_value, value=0,
                                     relief="groove", bd=3, tristatevalue="x", command=self.listbox_update)
        radio_btn_1.place(relx=0.0, rely=0.00, relheight=0.05, relwidth=0.5)
        radio_btn_2 = tk.Radiobutton(frm_list, text="Vars", variable=self.radio_value, value=1,
                                     relief="groove", bd=3, tristatevalue="x", command=self.listbox_update)
        radio_btn_2.place(relx=0.5, rely=0.00, relheight=0.05, relwidth=0.5)
        radio_btn_1.select()

        # wyszukiwarka elementu w liscie
        ent_search_name = tk.Entry(frm_list)
        ent_search_name.insert(0, 'Search: "name"')
        ent_search_name.place(rely=0.05, relheight=0.05, relwidth=1)
        # ustawienie listy z scrollbarem
        self.lb_list = tk.Listbox(frm_list, selectmode=tk.SINGLE)
        self.lb_list.place(rely=0.10, relheight=0.85, relwidth=0.93)
        self.listbox_insert_data()
        sb_to_list = tk.Scrollbar(frm_list)
        sb_to_list.place(relx=0.93, rely=0.10, relheight=0.85, relwidth=0.07)
        self.lb_list.config(yscrollcommand=sb_to_list.set)
        sb_to_list.config(command=self.lb_list.yview)
        # pasek przyciskow dla CRUD
        btn_new_item = tk.Button(frm_list, text="New", bd=3, command=self.asd)
        btn_new_item.place(relx=0.00, rely=0.95, relwidth=0.33, relheight=0.05)
        btn_update_item = tk.Button(frm_list, text="Update", bd=3)
        btn_update_item.place(relx=0.33, rely=0.95, relwidth=0.34, relheight=0.05)
        btn_delete_item = tk.Button(frm_list, text="Delete", bd=3, command=self.listbox_delete)
        btn_delete_item.place(relx=0.67, rely=0.95, relwidth=0.33, relheight=0.05)

    def set_current_abb(self):
        """ Sets current abbreviation list for the obj.
        :return: None
        """
        self.current_abb = self.lsts[self.radio_value.get()]

    def listbox_insert_data(self):
        """ Insert data to the listbox to display it.
        :return: None
        """
        to_insert = []
        text = ""
        for i, item in enumerate(self.current_abb.elements):
            text += f"{i + 1}. "
            for j, v in enumerate(item.values()):
                if j:
                    text += f" - {v[:15]}"
                else:
                    text += f"{v}"
            to_insert.append(text)
            text = ""
        self.lb_list.insert(tk.END, *to_insert)

    def listbox_update(self):
        """ Triggered from radio buttons, sets current abbreviation list and switches content of the listbox.
        :return:
        """
        self.set_current_abb()  # update current abbreviation list
        self.lb_list.delete(0, tk.END)  # clear listbox content
        self.listbox_insert_data()  # display new data in listbox content

    def listbox_delete(self):
        """ Deletes focused row in listbox content and from current abbreviation list.
        :return:
        """
        idx = self.lb_list.curselection()[0]  # temp var for keeping current element focus
        item = self.current_abb.elements[idx]  # retrieve dict value from current abbreviation list
        try:
            # Delete part
            self.lb_list.delete(tk.ANCHOR)  # deletes current focused element in listbox
            delete_dict(item, self.current_abb.elements)  # validation checks, if passed value deleted from list
            if self.current_abb.name == "abbreviation":
                keyboard.add_abbreviation(item['string_to_write'], item['string_to_write'])  # restore to default from abbreviation
            else:
                [set_abbreviation(element, *self.current_abb.elements) for element in self.abbreviation.elements]  # clears abbreviations using this overwrite abbreviation
            write_to_json(self.current_abb.path, self.current_abb.elements)  # save changes to json

            # Update listbox display
            self.listbox_update()  # Displays actual content in the listbox
            self.lb_list.selection_set(idx)  # leaves focus on the same row index
            # if len list becomes shorter that current focused index then lower index is focused
            if not self.lb_list.selection_includes(idx):
                # dunno why but both focusses must be set for correct working
                self.lb_list.selection_set(idx - 1)
                self.lb_list.selection_anchor(idx - 1)
        except:
            return
        # lb_list --> lb_content?


    def asd(self):
        self.idx = self.lb_list.curselection()
        print(f"Selected idx: {self.idx[0]}, type: {type(self.idx)}")
        # czyszczenie
        print(self.lb_list.selection_clear(3, tk.END))
        # sprawdzenie zaznaczenia
        print(f"Last element selected: {self.lb_list.selection_includes(tk.END)}")
        self.lb_list.selection_set(0, 0)
        self.lb_list.activate(0)
        print(f"Selected idx: {self.idx[0]}, type: {type(self.idx)}")


    # przechodzenie z listy ostatni->pierwszy, pierwszy->ostatni