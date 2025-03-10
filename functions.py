FILEPATH ="todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as filey:
        todos_y = filey.readlines()
    return todos_y

def write_todos(todos_arg,filepath=FILEPATH):
    with open(filepath,'w')as file_local:
        file_local.writelines(todos_arg)

if __name__ ==" __main__":
    print("hello")