import time
import ast
import os

FILEPATH = "todos.txt"

todos = []
fail_count = 0

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            todos_list = f.readlines()
    else:
        todos_list = []
    return todos_list


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.write("".join(todos_arg))