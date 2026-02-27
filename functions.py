import time
import ast
import os

FILEPATH = "todos.txt"
RECYLCE_FILE = "recycle_bin.txt"
EXPIRY_SECONDS = 24 * 3600  # 24 hours


def load_recycle():
    if os.path.exists(RECYLCE_FILE):
        with open(RECYLCE_FILE, "r") as f:
            try:
                return ast.literal_eval(f.read() or "[]")
            except Exception:
                return []
    return []

def save_recycle(rb):
    with open(RECYLCE_FILE, "w") as f:
        f.write(str(rb))

def cleanup_expired(rb, expiry_seconds=EXPIRY_SECONDS):
    now = time.time()
    kept = [item for item in rb if now - item.get("deleted_at", 0) < expiry_seconds]
    if len(kept) != len(rb):
        save_recycle(kept)
    return kept

# load recycle bin at start and remove expired items
recycle_bin = load_recycle()
recycle_bin = cleanup_expired(recycle_bin)

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
    

def get_recycle():#type:ignore
        if os.path.exists("recycle_bin.txt"):
            with open("recycle_bin.txt", "w") as f:
                f.write(str(recycle_bin))
        else:
            with open("recycle_bin.txt", "a") as f:
                f.write(str(recycle_bin))


def timer_finished_action(recycle_bin, todo_to_delete):
    if todo_to_delete in recycle_bin:
        recycle_bin.remove(todo_to_delete)
        with open("recycle_bin.txt", "w") as f:
            f.write(str(recycle_bin))


def countdown(seconds, recycle_bin, todo_to_delete):
    while seconds > 0:
        time.sleep(1)
        seconds -= 1
    timer_finished_action(recycle_bin, todo_to_delete)