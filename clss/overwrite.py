import json

from clss.error_cls import *


class AbbOverwrite:
    """
    Object which replace found "name" string in given
    location with own "text" string value.
    """
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f"{self.__class__.__name__}(Name={self.name}, Text={self.text})"


class AbbsOverwrite:
    """ CRUD for the AbbOverwrite objects. """
    elements = []

    def __init__(self, path):
        self.path = path
        self.elements = self.load_elements()

    def element_in(self, abb_overwrite):
        """
        Checks if there is already given Abb object in self.elements list.

        :param abb_overwrite: abb_overwrite object looked for
        :return: True if found else False
        """
        if abb_overwrite in self.elements:
            return True
        return False

    def element_name_in(self, abb_overwrite_name):
        """
        Checks if there is already any Abb object with
        given name attribute in self.elements list.

        :param abb_overwrite_name: name attribute looked for.
        :return: True if found, else False
        """
        for abb in self.elements:
            if abb.name == abb_overwrite_name:
                return True
        return False

    def add_element(self, new_element_name, new_element_text):
        """
        Creates new Abb object and add it to the
        self.elements list if validation is passed.

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
        self.elements.append(AbbOverwrite(new_element_name, new_element_text))
        self.save_elements()

    def update_element(self, abb_overwrite, updated_name, updated_text):
        """
        Updates given Abb object with new attributes if their validation is passed.

        :param abb_overwrite: to be updated
        :param updated_name: new name value
        :param updated_text: new text value
        """
        if not self.element_in(abb_overwrite):
            raise SomethingIsNotYes
        if updated_name is "" and updated_text is "":
            raise FillBothEntries
        elif updated_name is "":
            raise FillName
        elif updated_text is "":
            raise FillText

        element_index = self.elements.index(abb_overwrite)
        self.elements.remove(abb_overwrite)

        if self.element_name_in(updated_name):
            self.elements.insert(element_index, abb_overwrite)
            raise NameAlreadyUsed

        self.elements.insert(element_index, AbbOverwrite(updated_name, updated_text))
        self.save_elements()

    def delete_element(self, abb_overwrite):
        """
        Deletes given Abb object from the self.elements list.

        :param abb_overwrite: abb_overwrite objected to be deleted
        """
        if self.element_in(abb_overwrite):
            self.elements.remove(abb_overwrite)
            self.save_elements()
        else:
            raise SomethingIsNotYes

    def load_elements(self):
        """
        Creates from loaded json a list of Abb objects saved under self.elements.

        :return: Abb(s) list
        """
        raw_data = self.read_json(self.path)['elements']
        return [AbbOverwrite(element["name"], element["text"]) for element in raw_data]

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