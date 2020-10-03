from tkinter import *

root = Tk()

asd = "Hello from asd"

menubar = Menu(root)

salutations = Menu(menubar, tearoff=False)
salutations.add_command(label="Say Hello", command=lambda: print(asd))
salutations.add_command(label="Say Goodbye", command=lambda: print("Goodbye"))
menubar.add_cascade(label="Salutations", menu=salutations)

option_1 = StringVar()
option_2 = StringVar()
radio_option = StringVar()

options = Menu(menubar, tearoff=False)
options.add_checkbutton(label="Option 1", variable=option_1, command=lambda: print(option_1.get()))
options.add_checkbutton(label="Option 2", variable=option_2, command=lambda: print(option_2.get()))
options.add_separator()
options.add_radiobutton(label="Radio 1", variable=radio_option, value="Radio Option 1")
options.add_radiobutton(label="Radio 2", variable=radio_option, value="Radio Option 2")
options.add_radiobutton(label="Radio 3", variable=radio_option, value="Radio Option 3")

menubar.add_cascade(label="Options", menu=options)




root.config(menu=menubar)

root.mainloop()
