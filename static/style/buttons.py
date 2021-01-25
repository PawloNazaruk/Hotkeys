from tkinter import ttk


def set_buttons_styles():
    """
    Function creates styles for submit and cancel buttons.
    Accordingly green and red background will be added to them.
    """
    style = ttk.Style()
    style.configure(
        'Submit.TButton',
        font=('calibri', 10, 'bold'),
        background='#00FF00',
    )
    style.configure(
        'Cancel.TButton',
        font=('calibri', 10, 'bold'),
        background='#FF0000',
    )