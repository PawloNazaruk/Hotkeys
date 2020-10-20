import json
import keyboard
from CRUD import *


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
    """Creating new overridden tag from the user input and saving it in json file.

    :param my_list: when my_dict will become created as tag, then is added to tag common list
    :param override_list: list with dict(s) which will modify my_dict if they are in it
    :param new_dict: dict which will be modified
    :param path: json directory
    :return:
    """
    add_dict(my_list, new_dict)  # Dict data validation
    create_override_abbreviation(override_list, new_dict)  # Modification of the dict by other dicts
    write_to_json(path, my_list)


def update_tag(my_list, override_list, current_dict, new_dict, path):
    """Modifies data of the created tag with new values if requirements are met, then overriding it
    once again with modification data and saving it to the


    :param my_list:
    :param override_list:
    :param current_dict:
    :param new_dict:
    :param path:
    :return:
    """
    update_dict(my_list, current_dict, new_dict)
    create_override_abbreviation(override_list, new_dict)
    write_to_json(path, my_list)


def delete_tag(my_list, my_dict, path):
    # Atm keyboard library doesn't give option to update/delete made abbreviation,
    # so in order to delete it, it's behavior replacement_text is written as own name
    delete_dict(my_list, my_dict)
    keyboard.add_abbreviation(my_dict['name'], my_dict['name'])
    write_to_json(path, my_list)