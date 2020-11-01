import tkinter as tk


class MyListbox(tk.Listbox):
    """ Modified Listbox widget with methods for:
     handling displayed content, CRUD and
     walking with keyboard shortcuts over its content """
    def __init__(self, elements, *args, **kwargs):
        super().__init__(*args, elements, **kwargs)
        #self.bind('<<ListboxSelect>>', self.on_lb_click)
        self.bind("<Up>", self.on_press_move_up)
        self.bind("<Down>", self.on_press_move_down)
        self.elements = []

    def delete_element(self):
        """ Deletes element from the list and updates displayed element in the list box.

        :return:
        """
        element = self.elements.pop(self.curselection_index())
        self.delete(0, tk.END)
        self.insert_elements(self.elements)
        return element

    def insert_elements(self, elements):
        """ Takes given list of elements and updates displayed elements in the list box.

        :return:
        """
        self.delete(0, tk.END)
        self.elements = elements
        for index, element in enumerate(self.elements, 1):
            text = f"{index}. {self.make_pattern((element.name, element.text))}"
            self.insert(tk.END, text)

    @classmethod
    def make_pattern(cls, args):
        """ Sets up how each element will be displayed in the list box.

        :param args: various strings
        :return: one formated string
        """
        text = []
        for arg in args:
            print(f"arg: {arg}")
            text.append(f"{arg} - ")
        return " ".join(text)[:-3].rstrip()[:40]

    def curselection_index(self):
        """ Returns currently selection as index.

        :return: index
        """
        return int(self.curselection()[0])

    def curselection_value(self):
        """ Return currently selection as value.

        :return: abb/abb_overwrite object
        """
        return self.elements[self.curselection()[0]]

    def on_press_move_up(self, evt):
        """ Moves currently selection upwards by pressing "UP" keyboard button.

        :param evt: keyboard button.
        :return:
        """
        w = evt.widget
        index = w.curselection()[0]
        self.selection_clear(0, tk.END)
        if index == 0:
            self.selection_set(tk.END)
        else:
            self.selection_set(index - 1)

    def on_press_move_down(self, evt):
        """ Moves currently selection upwards by pressing "DOWN" keyboard button.

        :param evt: event created after clicking "Down" keyboard button.
        :return:
        """
        w = evt.widget
        index = w.curselection()[0]
        self.selection_clear(0, tk.END)
        if len(self.get(index, tk.END)) == 1:
            self.selection_set(0)
        else:
            self.selection_set(index + 1)
