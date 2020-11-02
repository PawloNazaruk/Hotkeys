import json
import keyboard
from clss.error_cls import *


class Abb:
    """ Abbreviation object which changes written "name" value to the "text".
    It's "text" value can be also modified by AbbOverwrite objects. """
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def set_abbreviation(self, abbs_overwrite_elements):
        """
        Sets new abbreviation matching when writing "name"->"text".

        :param abbs_overwrite_elements: list of AbbsOverwrite objects which can modify "text" value.
        """

        overwrite_occured = 0
        for abb_overwrite in abbs_overwrite_elements:
            if abb_overwrite.name in self.text:
                modified_text = self.text.replace(abb_overwrite.name, abb_overwrite.text)
                keyboard.add_abbreviation(self.name, modified_text)
                overwrite_occured = 1
        if not overwrite_occured:
            keyboard.add_abbreviation(self.name, self.text)

    def update_abbreviation(self, abbs_overwrite_elements):
        """
        Turning off old abbreviation matching, ane sets a new one.

        :param abbs_overwrite_elements: list of AbbsOverwrite objects which can modify "text" value.
        """
        keyboard.remove_word_listener(self.name)
        self.set_abbreviation(abbs_overwrite_elements)

    def delete_abbreviation(self):
        """
        Clears current abbreviation matching.
        """
        keyboard.remove_word_listener(self.name)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f"{self.__class__.__name__}(Name={self.name}, Text={self.text})"


class Abbs:
    """
    CRUD for the Abb objects.
    """
    elements = []

    def __init__(self, path, abbs_overwrite_elements):
        self.path = path
        self.abb_overwrite_elements = abbs_overwrite_elements
        self.elements = self.load_elements()
        self.set_all_abbreviation(abbs_overwrite_elements)

    def set_all_abbreviation(self, abbs_overwrite_elements):
        [abb.set_abbreviation(abbs_overwrite_elements) for abb in self.elements]

    def element_in(self, element):
        """
        Checks if there is already given Abb object in self.elements list.

        :param element: Abb object looked for.
        :return: True if found else False
        """
        if element in self.elements:
            return True
        return False

    def element_name_in(self, element_name):
        """
        Checks if there is already any Abb object with given name attribute in self.elements list.

        :param element_name: name attribute looked for.
        :return: True if found, else False
        """
        for abb in self.elements:
            if abb.name == element_name:
                return True
        return False

    def add_element(self, new_element_name, new_element_text):
        """
        Creates new Abb object and add it to the self.elements list
        if validation is passed and it's abbreviation matching.

        :param new_element_name: name attribute
        :param new_element_text: text attribute
        """
        if new_element_name is "" and new_element_text is "":
            raise FillBothEntries
        elif new_element_name is "":
            raise FillName
        elif new_element_text is "":
            raise FillText
        elif self.element_name_in(new_element_name):
            raise NameAlreadyUsed
        abb = Abb(new_element_name, new_element_text)
        abb.set_abbreviation(self.abb_overwrite_elements)  # Sets active matching "name"->"text"
        self.elements.append(abb)
        self.save_elements()

    def update_element(self, abb, updated_name, updated_text):
        """
        Updates given Abb object with new attributes if their
        validation is passed and it's abbreviation matching.

        :param abb: to be updated
        :param updated_name: new name value
        :param updated_text: new text value
        """
        if not self.element_in(abb):
            raise SomethingIsNotYes
        if updated_name is "" and updated_text is "":
            raise FillBothEntries
        elif updated_name is "":
            raise FillName
        elif updated_text is "":
            raise FillText


        element_index = self.elements.index(abb)
        self.elements.remove(abb)

        if self.element_name_in(updated_name):
            self.elements.insert(element_index, abb)
            raise NameAlreadyUsed

        new_abb = Abb(updated_name, updated_text)
        new_abb.update_abbreviation(self.abb_overwrite_elements)  # Sets active matching "name"->"text"
        self.elements.insert(element_index, new_abb)
        self.save_elements()

    def delete_element(self, abb):
        """
        Deletes given Abb object from the self.elements
        list and it's abbreviation matching.

        :param abb: Abb objected to be deleted
        """
        if self.element_in(abb):
            abb.delete_abbreviation()  # Sets matching as "name" -> "name"
            self.elements.remove(abb)
            self.save_elements()
        else:
            raise SomethingIsNotYes

    def load_elements(self):
        """
        Creates from loaded json a list of Abb
        objects saved under self.elements.

        :return: Abb(s) list
        """
        raw_data = self.read_json(self.path)['elements']
        return [Abb(element["name"], element["text"]) for element in raw_data]

    def save_elements(self):
        """
        Unpacks Abb objects from self.elements list to save them in json.
        """
        temp_elements = [{"name": abb.name, "text": abb.text} for abb in self.elements]
        self.write_to_json(self.path, temp_elements)

    @staticmethod
    def read_json(path):
        """
        Reads content from the json file.

        :param path: path to the file
        """
        with open(path, "r") as file_ref:
            raw_data = json.load(file_ref)
            return raw_data

    @staticmethod
    def write_to_json(path, my_list):
        """
        Writes content of the my_list to the json file.

        :param path: path to the file
        :param my_list: list of dicts
        """
        with open(path, "r+") as file_ref:
            file_ref.seek(0)
            json.dump(dict(elements=my_list), file_ref, indent=4)
            file_ref.truncate()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.elements})"