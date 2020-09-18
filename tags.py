import json
import keyboard
from pprint import pprint

def get_tag_template(path = "template\\tags.json"):
    with open(path, "r") as file_ref:
        raw_data = json.load(file_ref)
        return raw_data

def set_tag_template(tags, path = "template\\tags.json"):
    with open(path, "r+") as file_ref:
        file_ref.seek(0)
        json.dump(dict(tags=tags), file_ref, indent=4)
        file_ref.truncate()

def tag_exist(tags, myDict):
    for tag in tags:
        if myDict == tag:
            return "Tag exist."
    return 0

def tag_key_exist(tags, myDict):
    for tag in tags:
        if myDict['name'] == tag['name']:
            return "Tag exist."
    return 0

def create_tag(tags, myDict):
    if myDict["name"] is "" or myDict["switch_to"] is "":
        return "Fill both entries."
    if tag_key_exist(tags, myDict):
        return "Name is already used."

    tags.append(myDict)
    keyboard.add_abbreviation(myDict["name"], myDict["switch_to"])
    print("Tag created.")
    set_tag_template(tags)
    return "Tag created."

def update_tag(tags, myDict, newDict):
    if not tag_exist(tags, myDict):
        return "Tag doesn't exist."

    tags.pop(tags.index(myDict))
    print(f'myDict: {myDict}')
    print(f'newDict: {newDict}')
    if tag_key_exist(tags, newDict):
        tags.append(myDict)
        return "The name is already used in another tag."

    tags.append(newDict)
    keyboard.add_abbreviation(myDict['name'], myDict['name'])
    keyboard.add_abbreviation(newDict['name'], myDict['switch_to'])
    print("Tag was updated.")
    set_tag_template(tags)
    return "Tag updated."

def delete_tag(tags, myDict):
    if not tag_exist(tags, myDict):
        return "Tag to delete doesn't exist."

    pprint(f"delete_tag: {tags}")
    tags.pop(tags.index(myDict))
    pprint(f"delete_tag after: {tags}")
    keyboard.add_abbreviation(myDict['name'], myDict['name'])
    print("Tag was deleted.")
    set_tag_template(tags)
    return "Tag deleted."

def create_abbreviation_from_file(tags, vars):
    # TODO Comprehension??
    for myDict in tags:
        status = 'to_create'
        for var in vars:
            for key, val in var.items():
                if myDict['switch_to'] == key:
                    myDict['switch_to'] = myDict['switch_to'].replace(key, val)
                    print(myDict)
                    keyboard.add_abbreviation(myDict['name'], myDict['switch_to'])
                    status = 'created'
        if status == 'to_create':
            keyboard.add_abbreviation(myDict['name'], myDict['switch_to'])