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

def tag_exist(tags, dict):
    for tag in tags:
        if dict['name'] == tag['name']:
            return 'exist'
    return None

def create_tag(tags, dict):
    if tag_exist(tags, dict) == None:
        tags.append(dict)
        keyboard.add_abbreviation(dict["name"], dict["switch_to"])
        print("Tag created.")
        set_tag_template(tags)
    else:
        print("Tag couldn't be created, as is already existing.")

def update_tag(tags, dict, new_dict):
    if tag_exist(tags, dict) != None:
        tags.pop(tags.index(dict))
        if tag_exist(tags, new_dict) == None:
            tags.append(new_dict)
            keyboard.add_abbreviation(dict['name'], "Tag will be cleared with the new start of the program.")
            keyboard.add_abbreviation(dict['name'], dict['switch_to'])
            print("Tag was updated.")
            set_tag_template(tags)
        else:
            print("The name of the tag is already used.")
    else:
        print("Tag couldn't be found.")

def delete_tag(tags, dict):
    if tag_exist(tags, dict) != None:
        tags.pop(tags.index(dict))
        keyboard.add_abbreviation(dict['name'], "Tag will be cleared with the new start of a program.")
        print("Tag was deleted.")
        set_tag_template(tags)
    else:
        print("Tag to delete doesn't exist.")



def main():
    tags = get_tag_template()['tags']
    create_tag(tags, dict(name = "667", switch_to = "777"))
    pprint(tags)
    #update_tag(tags, dict(name = "667", switch_to = "112"), dict(name = "667", switch_to = "333"))
    #pprint(tags)
    delete_tag(tags, dict(name = "667", switch_to = "333"))
    pprint(tags)


if __name__ == "__main__":
    main()