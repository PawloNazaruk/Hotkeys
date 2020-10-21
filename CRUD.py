import json


class BaseValidationError(ValueError):
    """ Class for marking errors
    """
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
    :return:
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
        json.dump(dict(elements=my_list), file_ref, indent=4)
        file_ref.truncate()


def dict_in_list(my_list, searched_dict):
    """THe function checks if the searched value can be added to the list as unique record.

    :param my_list: list containing dict(s)
    :param searched_dict: dict for comparison
    :return: 0 when searched_dict is in my_list
    """
    for d in my_list:
        if searched_dict == d:
            return 0
    raise DictDoesntExistInList


def dict_duplicated_key_in_list(my_list, searched_dict, key):
    """The function confirms if searched value won't become duplicate in the list.

    :param my_list: list containing dict(s)
    :param searched_dict: dict for comparison
    :param key: specified key of the searched_dict
    :return: 0 when dict with this name doesn't exist
    """
    for d in my_list:
        if searched_dict[key] == d[key]:
            raise DictWithNameAlreadyUsed
    return 0


def add_dict(my_list, new_dict):
    """If dict meets requirements of not empty values then is added to the list.

    :param my_list: list containing dict(s)
    :param new_dict: dict which will be added
    :return:
    """
    if new_dict["name"] is "" and new_dict["switch_to"] is "":
        raise FillBothEntries
    elif new_dict["name"] is "":
        raise FillName
    elif new_dict["switch_to"] is "":
        raise FillSwitchTo
    elif dict_duplicated_key_in_list(my_list, new_dict, "name"):
        raise DictWithNameAlreadyUsed
    my_list.append(new_dict)


def update_dict(my_list, current_dict, new_dict):
    """Searches for specific current_tag dict in the tags list,
    when found updates its content with new_tag dict.

    :param my_list: list containing dict(s)
    :param current_dict: dict which content will be changed
    :param new_dict: overwrites current_tag content with own data
    :return:
    """
    if dict_in_list(my_list, current_dict):
        raise DictDoesntExistInList

    current_dict_index = my_list.index(current_dict)
    temp_list = my_list[:current_dict_index] + my_list[current_dict_index + 1:]
    if dict_duplicated_key_in_list(temp_list, new_dict, "name"):
        raise DictWithNameAlreadyUsed

    my_list.pop(current_dict_index)
    my_list.append(new_dict)


def delete_dict(my_dict, my_list):
    """Deleting given dict from the list and json file at given path.

    :param my_list: list containing dict(s)
    :param my_dict: dict which will be deleted
    :return:
    """
    if dict_in_list(my_list, my_dict):
        raise DictDoesntExistInList

    my_list.pop(my_list.index(my_dict))