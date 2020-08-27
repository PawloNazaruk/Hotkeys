import json
import keyboard
from pprint import pprint


def get_tag_template(path = "template\\tags.json"):
    with open(path, "r") as file_ref:
        raw_data = json.load(file_ref)
        return raw_data

def set_tag_template(updated_dict, path = "template\\tags.json"):
    with open(path, "r+") as file_ref:
        json.dump(updated_dict, file_ref, indent=4, sort_keys=True)

def is_duplicate(lst, dict):
    if not dict['write'] in lst:
        return 'pass'
    return 'duplicate'

def create_tag(all_tags, dict):
    all_tags.append(dict)
    keyboard.add_abbreviation(dict["write"], dict["switch_to"])

def retrive_tag(all_tags, key='Beniz'):
    print("ASDDDD")
    for asd in all_tags:
        print(asd)

def update_tag(all_tags, dict, newDict):




def main():
    all_tags = get_tag_template()['tags']
    #pprint(all_tags)
    #pprint(is_duplicate(all_tags, {'switch_to': '[currentBuild]', 'write': '@build'}))

    create_tag(all_tags, dict(write = "666", switch_to = "777"))

    print(retrive_tag(all_tags, 'Beniz'))

if __name__ == "__main__":
    main()