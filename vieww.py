import tkinter as tk
from tags import *

class MyApp:
    def __init__(self, root, tags, effectors):
        self.root = root
        self.tags = tags
        self.effectors = effectors
        self.lst_temp = [x for x in range(101)]
        self.display_menubar()
        self.display_home(tags, effectors)

    def display_menubar(self):
        menubar = tk.Menu(self.root)
        menubar.add_command(label="Home", command=lambda: print("Home"))
        menubar.add_command(label="reg", command=lambda: print("reg"))
        self.root.config(menu=menubar)

    def display_home(self, tags, effectors):
        self.current_list = tk.IntVar()
        self.list_container = [
            tags,  # radio button focusses it with 0
            effectors,  # radio button foccuses it with 1
        ]


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
        radio_btn_1 = tk.Radiobutton(frm_list, text="Tags", variable=self.current_list, value=0,
                                     relief="groove", bd=3, tristatevalue="x", command=self.listbox_update)
        radio_btn_1.place(relx=0.0, rely=0.00, relheight=0.05, relwidth=0.5)
        radio_btn_2 = tk.Radiobutton(frm_list, text="Vars", variable=self.current_list, value=1,
                                     relief="groove", bd=3, tristatevalue="x", command=self.listbox_update)
        radio_btn_2.place(relx=0.5, rely=0.00, relheight=0.05, relwidth=0.5)
        radio_btn_1.select()
        print(self.current_list.get())

        # wyszukiwarka elementu w liscie
        ent_search_name = tk.Entry(frm_list)
        ent_search_name.insert(0, 'Search: "name"')
        ent_search_name.place(rely=0.05, relheight=0.05, relwidth=1)
        # ustawienie listy z scrollbarem
        self.lb_list = tk.Listbox(frm_list, selectmode=tk.SINGLE)
        self.lb_list.place(rely=0.10, relheight=0.85, relwidth=0.93)
        self.listbox_insert()
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

    def listbox_insert(self):
        to_insert = [f"{i + 1}. {my_dict['name']}" for i, my_dict in enumerate(self.list_container[self.current_list.get()])]
        self.lb_list.insert(tk.END, *to_insert)

    def listbox_update(self):
        self.lb_list.delete(0, tk.END)
        self.listbox_insert()

    def listbox_delete(self):


        self.idx = self.lb_list.curselection()[0]  # temp var for keeping current element focus
        self.lb_list.delete(tk.ANCHOR)  # deletes current focused element
        self.my_dict = self.list_container[self.current_list.get()][self.idx - 1]
        delete_tag(self.tags, self.my_dict, "template\\vars.json")

        self.lb_list.selection_set(self.idx)  # sets focus to the same row index
        # if len list becomes shorter that current focused index then lower index is focused
        if not self.lb_list.selection_includes(self.idx):
            # dunno why but both focusses must be set for correct working
            self.lb_list.selection_set(self.idx - 1)
            self.lb_list.selection_anchor(self.idx - 1)



        # zapis do pliku
        # self.listbox_update()


        #self.lb_list.selection_set(self.idx - 1)



        """if not self.lb_list.selection_includes(self.idx):
            self.lb_list.selection_set(self.idx - 1)
        
        """




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