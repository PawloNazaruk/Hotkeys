import json
from pprint import pprint


def read_template(path = "template\\tags.json"):
    with open(path, "r") as file_ref:
        d = json.load(file_ref)
        return d

def update_template(updated_dict, path = "template\\tags.json"):
    with open(path, "r+") as file_ref:
        json.dump(updated_dict, file_ref, indent=4, sort_keys=True)


def main():

    all_categories = read_template()
    pprint(all_categories)

    all_categories["new"] = "asd"
    all_categories["tags"].append(dict(write = "123", switch_to = "321"))
    update_template(all_categories)
    pprint(read_template())


if __name__ == "__main__":
    main()