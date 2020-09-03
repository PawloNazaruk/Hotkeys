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
        json.dump(dict(tags=tags), file_ref, indent=4, sort_keys=True)
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
    if myDict["name"] is None or myDict["switch_to"] is None:
        return "Fill both entries."
    if tag_key_exist(tags, myDict):
        return "Name is already used."

    tags.append(myDict)
    keyboard.add_abbreviation(myDict["name"], myDict["switch_to"])
    print("Tag created.")
    set_tag_template(tags)


def update_tag(tags, myDict, new_dict):
    if tag_exist(tags, myDict) != None:
        tags.pop(tags.index(myDict))
        if tag_key_exist(tags, new_dict) == None:
            tags.append(new_dict)
            keyboard.add_abbreviation(myDict['name'], "Tag will be cleared with the new start of the program.")
            keyboard.add_abbreviation(myDict['name'], myDict['switch_to'])
            print("Tag was updated.")
            set_tag_template(tags)
        else:
            print("The name of the tag is already used.")
    else:
        print("Tag couldn't be found.")

def delete_tag(tags, myDict):
    if tag_exist(tags, myDict) != None:
        tags.pop(tags.index(myDict))
        keyboard.add_abbreviation(myDict['name'], "Tag will be cleared with the new start of a program.")
        print("Tag was deleted.")
        set_tag_template(tags)
    else:
        print("Tag to delete doesn't exist.")

def create_abbreviation_from_file(tags, vars):
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



def main():
    tags = get_tag_template("template\\tags.json")['tags']
    vars = get_tag_template("template\\vars.json")['vars']

    asd = dict(name="asd456", switch_to="qwe")

    create_tag(tags, asd)
    #print(create_tag(tags, asd))

    create_abbreviation_from_file(tags, vars)


    while True:
        continue






if __name__ == "__main__":
    main()