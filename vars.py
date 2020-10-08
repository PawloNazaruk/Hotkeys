from CRUD import *


def add_var(my_list, new_dict, path):
    add_dict(my_list, new_dict)
    write_to_json(path, my_list)


def update_var(my_list, current_dict, new_dict, path):
    update_dict(my_list, current_dict, new_dict)
    write_to_json(path, my_list)


def delete_var(my_list, my_dict, path):
    delete_dict(my_list, my_dict)
    write_to_json(path, my_list)