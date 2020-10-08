from tags import create_override_abbreviation
from view import *

PATH_TAGS = "template\\tags.json"
PATH_VARS = "template\\vars.json"


def main():
    tags = read_json(PATH_TAGS)['my_data']
    override_list = read_json(PATH_VARS)['my_data']

    for my_dict in tags:
        create_override_abbreviation(override_list, my_dict)

    root = Tk()
    root.geometry("800x600")
    root.title("Hotkeys")
    myapp = MyApp(root, tags, override_list)

    root.mainloop()


if __name__ == "__main__":
    main()
