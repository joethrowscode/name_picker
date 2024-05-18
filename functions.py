FILEPATH = "names.txt"
import random


def get_names(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        names_local = file_local.readlines()
    return names_local


def write_names(names_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(names_arg)



