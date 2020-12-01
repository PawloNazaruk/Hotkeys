import tkinter as tk

from clss.normal import Abbs
from clss.overwrite import AbbsOverwrite
from view.abbreviation_manager import MyApp


PATH_ABBOVERWRITE = "template/abboverwrite_elements.json"
PATH_ABB = "template/abb_elements.json"


def main():
    abbs_overwrite = AbbsOverwrite(PATH_ABBOVERWRITE)
    abbs = Abbs(PATH_ABB, abbs_overwrite.elements)

    root = tk.Tk()
    root.geometry("800x600")
    root.title("Peon")
    root.iconbitmap('img/peon.ico')
    myapp = MyApp(root, abbs, abbs_overwrite)

    root.mainloop()


if __name__ == "__main__":
    main()
