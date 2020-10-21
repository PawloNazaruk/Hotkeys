import json
import keyboard
from CRUD import *


def set_abbreviation(item, *overwrite_list):
    """ Create abbreviation from the item, could by updated by overwrite element value.

    :param item: base for creating abbreviation ['string_to_write'] -> ['replace_to'] values
    :param overwrite_list: list of elements which can update
            item['replace_to'] by its own ['string_to_find'] - ['replace_to'] values
    :return: None
    """
    overwrite_done = 0
    for overwrite_element in overwrite_list:
        if overwrite_element['string_to_find'] in item['replace_to']:
            item_replace_to_updated = item['replace_to']\
                .replace(overwrite_element['string_to_find'], overwrite_element['replace_to'])
            keyboard.add_abbreviation(item['string_to_write'], item_replace_to_updated)
            overwrite_done = 1

    if not overwrite_done:
        keyboard.add_abbreviation(item['string_to_write'], item['replace_to'])


def new_abbreviation_element(my_list, overwrite_list, new_dict, path):
    """Creating new overridden tag from the user input and saving it in json file.
    """
    add_dict(my_list, new_dict)  # Dict data validation
    set_abbreviation(new_dict, overwrite_list)  # Modification of the dict by other dicts
    write_to_json(path, my_list)


def update_abbreviation_element(my_list, override_list, current_dict, new_dict, path):
    """Modifies data of the created tag with new values if requirements are met, then overriding it
    once again with modification data and saving it to the
    """
    update_dict(my_list, current_dict, new_dict)
    set_abbreviation(override_list, new_dict)
    write_to_json(path, my_list)


def delete_abbreviation_element(my_list, my_dict, path):
    # Atm keyboard library doesn't give option to update/delete made abbreviation,
    # so in order to delete it, it's behavior replacement_text is written as own name
    delete_dict(my_dict, my_list)
    keyboard.add_abbreviation(my_dict['name'], my_dict['name'])
    write_to_json(path, my_list)