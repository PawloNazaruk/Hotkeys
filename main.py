from tags import set_abbreviation
from CRUD import *
from vieww import *
from collections import namedtuple
from pprint import pprint

PATH_ABBREVIATION_ELEMENTS = "template/abbreviation_elements.json"
PATH_ABBREVIATION_OVERWRITE_ELEMENTS = "template/abbreviation_overwrite_elements.json"

# better name for \abbreviation_overwrite/??


def main():
    Content = namedtuple("Abbreviation", [
        "name",
        "elements",
        "path",
    ])

    abb_elements = read_json(PATH_ABBREVIATION_ELEMENTS)['elements']
    abb_overwrite_elements = read_json(PATH_ABBREVIATION_OVERWRITE_ELEMENTS)['elements']

    abbreviation = Content("abbreviation", abb_elements, PATH_ABBREVIATION_ELEMENTS)
    abbreviation_overwrite = Content("abbreviation_overwrite",abb_overwrite_elements, PATH_ABBREVIATION_OVERWRITE_ELEMENTS)

    [set_abbreviation(element, *abbreviation_overwrite.elements) for element in abbreviation.elements]

    root = tk.Tk()
    root.geometry("800x600")
    root.title("Peon")
    myapp = MyApp(root, abbreviation, abbreviation_overwrite)

    root.mainloop()


if __name__ == "__main__":
    main()
