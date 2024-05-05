FILENAME = "todo.txt" # the


def get_todos(filepath=FILENAME):
    """Read a text file and return a list of
    to-do item
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath=FILENAME):
    """write to-do items list in the text files"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")