from tags import *
from view import *


def main():

    path_tags = "template\\tags.json"
    path_vars = "template\\vars.json"
    # extracting list of dicts from json import data
    tags = read_json(path_tags)['my_data']
    variables = read_json(path_vars)['my_data']

    create_abbreviation(tags, variables)

    some_tag = dict(name="@Benon", switch_to="Beniz")
    another_tag = dict(asd="qwe", qwe="asd")

    print(tag_exist(tags, dict(name="@build", switch_to="Build12345678989")))

    try:
        add_tag(tags, some_tag)
    except FillBothEntries:
        print(f'Fill both entries.')
    except FillNameEntry:
        print(f'Name cannot be empty.')
    except FillSwitchToEntry:
        print(f'Switch to cannot be empty.')
    except TagNameAlreadyUsed:
        print('wutttttttt?')




    """
    root = Tk()
    root.geometry("800x600")
    root.title("Hotkeys")
    myapp = MyApp(root, tags)

    root.mainloop()
    """

if __name__ == "__main__":
    main()
