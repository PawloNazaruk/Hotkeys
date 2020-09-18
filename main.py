from tags import *
from view import *


def main():
    tags = get_tag_template("template\\tags.json")['tags']
    vars = get_tag_template("template\\vars.json")['vars']

    create_abbreviation_from_file(tags, vars)

    root = Tk()
    root.geometry("800x600")
    root.title("Hotkeys")
    myapp = MyApp(root, tags)

    root.mainloop()


if __name__ == "__main__":
    main()