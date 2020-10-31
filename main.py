from view.abbreviation_manager import *
from clss.normal import *
from clss.overwrite import *


PATH_ABBOVERWRITE = "template/abboverwrite_elements.json"
PATH_ABB = "template/abb_elements.json"


def main():
    abbs_overwrite = AbbsOverwrite(PATH_ABBOVERWRITE)
    abbs = Abbs(PATH_ABB, abbs_overwrite.elements)

    root = tk.Tk()
    root.geometry("800x600")
    root.title("Peon")
    myapp = MyApp(root, abbs, abbs_overwrite)

    root.mainloop()


if __name__ == "__main__":
    main()
