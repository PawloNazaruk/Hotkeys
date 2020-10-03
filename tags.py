import json
import keyboard
from pprint import pprint


class BaseValidationError(ValueError):
    pass


class DictDoesntExistInList(BaseValidationError):
    pass


class TagNameAlreadyUsed(BaseValidationError):
    pass


class FillNameEntry(BaseValidationError):
    pass


class FillSwitchToEntry(BaseValidationError):
    pass


class FillBothEntries(BaseValidationError):
    pass


class TagNameIsUsed(BaseValidationError):
    pass


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
            raise TagNameAlreadyUsed
    return 0


def add_tag(tags, new_tag):
    """Adds new_tag to the tags list if it doesn't already in it.

    :param tags: list containing dict(s)
    :param new_tag: tag dict to be added to the tags list
    :return:
    """
    if new_tag["name"] is "" and new_tag["switch_to"] is "":
        raise FillBothEntries
    elif new_tag["name"] is "":
        raise FillNameEntry
    elif new_tag["switch_to"] is "":
        raise FillSwitchToEntry
    elif tag_name_exist(tags, new_tag):
        raise TagNameAlreadyUsed

    tags.append(new_tag)
    # Creates new exchange from tag['name'] to tag['switch']
    keyboard.add_abbreviation(new_tag["name"], new_tag["switch_to"])
    write_to_json(path_tags)


def update_tag(tags, current_tag, new_tag):
    """Searches for specific current_tag dict in the tags list,
    when found updates its content with new_tag dict.

    :param tags: list containing dict(s)
    :param current_tag: tag dict which content will be changed
    :param new_tag: overwrites current_tag content with own
    :return:
    """

    try:
        tag_exist(tags, current_tag)
    except TagKeyDoesntExist as err:
        print(err.__name__)


    tags.pop(tags.index(current_tag))
    if tag_name_exist(tags, new_tag):
        tags.append(current_tag)
        return "The name is already used in another tag."

    tags.append(new_tag)
    keyboard.add_abbreviation(current_tag['name'], current_tag['name'])
    keyboard.add_abbreviation(new_tag['name'], current_tag['switch_to'])
    write_to_json(tags)


def delete_tag(tags, my_dict):
    if not tag_exist(tags, my_dict):
        return "Tag to delete doesn't exist."

    pprint(f"delete_tag: {tags}")
    tags.pop(tags.index(my_dict))
    pprint(f"delete_tag after: {tags}")
    keyboard.add_abbreviation(my_dict['name'], my_dict['name'])
    print("Tag was deleted.")
    set_json(tags)
    return "Tag deleted."


def create_abbreviation(tags, variables):
    for my_dict in tags:
        status = 'to_create'
        for var in variables:
            for key, val in var.items():
                if my_dict['switch_to'] == key:
                    my_dict['switch_to'] = my_dict['switch_to'].replace(key, val)
                    print(my_dict)
                    keyboard.add_abbreviation(my_dict['name'], my_dict['switch_to'])
                    status = 'created'
        if status == 'to_create':
            keyboard.add_abbreviation(my_dict['name'], my_dict['switch_to'])
