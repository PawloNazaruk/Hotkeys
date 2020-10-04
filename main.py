from tags import *
from view import *
from pprint import pprint
import time

PATH_TAGS = "template\\tags.json"
PATH_VARS = "template\\vars.json"


def main():

    # extracting list of dicts from json import data
    tags = read_json(PATH_TAGS)['my_data']
    variables = read_json(PATH_VARS)['my_data']

    create_abbreviation(tags, variables)

    benon_tag = dict(name="@Benon", switch_to="Beniz")
    another_tag = dict(name="PEPE", switch_to="SMALLU_PP")

    try:
        add_tag(tags, benon_tag, PATH_TAGS)
    except FillBothEntries as err:
        print(err.msg)
    except FillName as err:
        print(err.msg)
    except FillSwitchTo as err:
        print(err.msg)
    except DictWithNameAlreadyUsed as err:
        print(f'Cannot add: Name: {benon_tag["name"]} - {err.msg}')

    pprint(tags)
    time.sleep(10)
    print("UPDATED")
    """   
    try:
        update_tag(tags, benon_tag, another_tag, PATH_TAGS)
    except DictDoesntExistInList as err:
        print(f'{benon_tag} - {err.msg}')
    except DictWithNameAlreadyUsed as err:
        print(err.msg)
    pprint(tags)
    while True:
        pass
    """
    try:
        delete_tag(tags, benon_tag, PATH_TAGS)
    except DictDoesntExistInList as err:
        print(err.msg)



    while True:
        pass



    """
    root = Tk()
    root.geometry("800x600")
    root.title("Hotkeys")
    myapp = MyApp(root, tags)

    root.mainloop()
    """


if __name__ == "__main__":
    main()
