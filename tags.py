import json
import keyboard
from CRUD import *

#

def create_override_abbreviation(override_list, my_dict):
    """Function overwrite the given dict with matching values from dict(s) override_list.
    After all comparision and modification are done, then dict will become set as a tag*.
    As tag i mean that writing dict['name'] value will stimulate keyboard input to write
    in its place the dict['switch_to'] value.

    :param override_list: list with dict(s) which will modify my_dict if they are in it
    :param my_dict: dict which will be modified
    :return:
    """
    no_override = 1
    for d in override_list:
        if d['name'] in my_dict['switch_to']:
            override_switch_to = my_dict['switch_to'].replace(d['name'], d['switch_to'])
            keyboard.add_abbreviation(my_dict['name'], override_switch_to)
            no_override = 0

    if no_override:
        keyboard.add_abbreviation(my_dict['name'], my_dict['switch_to'])


def add_tag(my_list, override_list, new_dict, path):
    """ Creating new overridden tag from the user input and saving it in json file.

    :param my_list: when my_dict will become created as tag, then is added to tag common list
    :param override_list: list with dict(s) which will modify my_dict if they are in it
    :param new_dict: dict which will be modified
    :param path: json directory
    :return:
    """
    # Will be overwriting after writing ['name'] to the ['switch_to'] value
    add_dict(my_list, new_dict)
    create_override_abbreviation(override_list, new_dict)
    write_to_json(path, my_list)
    print(override_list)


def update_tag(my_list, override_list, current_dict, new_dict, path):
    update_dict(my_list, current_dict, new_dict)
    # Atm keyboard library doesn't give option to update/delete made abbreviation,
    # so in order to reset it, it's behavior replacement_text is written as own name
    keyboard.add_abbreviation(current_dict['name'], current_dict['name'])
    # Using new_dict to create updated abbreviation
    create_override_abbreviation(override_list, new_dict)
    write_to_json(path, my_list)


def delete_tag(my_list, my_dict, path):
    # Atm keyboard library doesn't give option to update/delete made abbreviation,
    # so in order to delete it, it's behavior replacement_text is written as own name
    delete_dict(my_list, my_dict)
    keyboard.add_abbreviation(my_dict['name'], my_dict['name'])
    write_to_json(path, my_list)








#def create_abbreviation(my_list):
    """Creates abbreviation for every dict in the given list.

    :param my_list: list containing dict(s)
    :return:
    """
    """for d in my_list:
        keyboard.add_abbreviation(d['name'], d['switch_to'])

    for d in my_list:
        status = 'to_create'
        for var in replacements_list:
            for key, val in var.items():
                if d['switch_to'] == key:
                    d['switch_to'] = d['switch_to'].replace(key, val)
                    print(d)
                    keyboard.add_abbreviation(d['name'], d['switch_to'])
                    status = 'created'
        if status == 'to_create':
            keyboard.add_abbreviation(d['name'], d['switch_to'])"""
