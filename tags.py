import json
import keyboard
from pprint import pprint


class BaseValidationError(ValueError):
    pass


class DictDoesntExistInList(BaseValidationError):
    msg = "Given dict doesn't exist in the list"


class DictWithNameAlreadyUsed(BaseValidationError):
    msg = "Given name is already used, use another one."


class FillName(BaseValidationError):
    msg = "Name cannot be empty."


class FillSwitchTo(BaseValidationError):
    msg = "Switch to cannot be empty."


class FillBothEntries(BaseValidationError):
    msg = "Fill Name and Switch To entries."


def read_json(path):
    """Import data from json in the given path.

    :param path: dir to the json file
    :return: whole data as dict() where value is list
    """
    with open(path, "r") as file_ref:
        raw_data = json.load(file_ref)
        return raw_data


def write_to_json(path, my_list):
    """Writes content of the my_list to the json file.

    :param path: dir to the json file
    :param my_list: list containing dict(s)
    :return:
    """
    with open(path, "r+") as file_ref:
        file_ref.seek(0)
        json.dump(dict(my_data=my_list), file_ref, indent=4)
        file_ref.truncate()


def dict_in_list(my_list, searched_dict):
    """Checks if dict is in list.

    :param my_list: list containing dict(s)
    :param searched_dict: dict for comparison
    :return: 0 when searched_dict is in my_list
    """
    for d in my_list:
        if searched_dict == d:
            return 0
    raise DictDoesntExistInList


def dict_name_in_list(my_list, searched_dict):
    """Checks if searched_dict['name'] already exist in the tags list.

    :param my_list: list containing dict(s)
    :param searched_dict: dict['key'] for comparison
    :return: 0 when dict with this name doesn't exist
    """
    for d in my_list:
        if searched_dict['name'] == d['name']:
            raise DictWithNameAlreadyUsed
    return 0


def add_tag(my_list, new_dict, path):
    """Adds new_tag to the tags list if it doesn't already in it.

    :param my_list: list containing dict(s)
    :param new_dict: dict to be added to the tags list when requirements are met
    :return:
    """
    if new_dict["name"] is "" and new_dict["switch_to"] is "":
        raise FillBothEntries
    elif new_dict["name"] is "":
        raise FillName
    elif new_dict["switch_to"] is "":
        raise FillSwitchTo
    elif dict_name_in_list(my_list, new_dict):
        raise DictWithNameAlreadyUsed

    my_list.append(new_dict)
    # Will be overwriting after writing ['name'] to the ['switch_to'] value
    keyboard.add_abbreviation(new_dict["name"], new_dict["switch_to"])
    write_to_json(path, my_list)


def update_tag(my_list, current_dict, new_dict, path):
    """Searches for specific current_tag dict in the tags list,
    when found updates its content with new_tag dict.

    :param my_list: list containing dict(s)
    :param current_dict: dict which content will be changed
    :param new_dict: overwrites current_tag content with own data
    :param path: dir to the json file
    :return:
    """

    if dict_in_list(my_list, current_dict):
        raise DictDoesntExistInList

    current_dict_index = my_list.index(current_dict)
    temp_list = my_list[:current_dict_index] + my_list[current_dict_index + 1:]
    if dict_name_in_list(temp_list, new_dict):
        raise DictWithNameAlreadyUsed

    my_list.pop(current_dict_index)
    my_list.append(new_dict)

    # Atm keyboard library doesn't give option to update/delete made abbreviation,
    # so in order to reset it, it's behavior replacement_text is written as own name
    keyboard.add_abbreviation(current_dict['name'], current_dict['name'])
    # Using new_dict to create updated abbreviation
    keyboard.add_abbreviation(new_dict['name'], new_dict['switch_to'])
    write_to_json(path, my_list)


def delete_tag(my_list, my_dict, path):
    """Deleting given dict from the list and json file at given path.

    :param my_list: list containing dict(s)
    :param my_dict: dict which will be deleted
    :param path: dir to the json file
    :return:
    """
    if dict_in_list(my_list, my_dict):
        raise DictDoesntExistInList

    my_list.pop(my_list.index(my_dict))
    # Atm keyboard library doesn't give option to update/delete made abbreviation,
    # so in order to delete it, it's behavior replacement_text is written as own name
    keyboard.add_abbreviation(my_dict['name'], my_dict['name'])
    write_to_json(path, my_list)


def 


def create_abbreviation(my_list):
    """The function creates abbreviation for every dict in the given list.

    :param my_list: list containing dict(s)
    :return:
    """
    for d in my_list:
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
            keyboard.add_abbreviation(d['name'], d['switch_to'])
