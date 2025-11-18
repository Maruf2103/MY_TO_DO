import os

FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read the text file and return a list of to-do items."""
    # Create the file if it doesn't exist
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass  # create empty file

    with open(filepath, 'r') as file:
        return file.readlines()


def write_todos(todos, filepath=FILEPATH):
    """Write the list of todos back into the file."""
    with open(filepath, 'w') as file:
        file.writelines(todos)


def add_todo(item, filepath=FILEPATH):
    """Add a new todo item to the file."""
    todos = get_todos(filepath)
    todos.append(item + "\n")
    write_todos(todos, filepath)


def remove_todo(index, filepath=FILEPATH):
    """Remove a todo by index (1-based)."""
    todos = get_todos(filepath)
    try:
        removed = todos.pop(index - 1)
        write_todos(todos, filepath)
        return removed.strip()
    except IndexError:
        return None


def search_todos(keyword, filepath=FILEPATH):
    """Return todos that contain the keyword."""
    todos = get_todos(filepath)
    return [todo.strip() for todo in todos if keyword.lower() in todo.lower()]


def clear_todos(filepath=FILEPATH):
    """Remove all todos."""
    write_todos([], filepath)


if __name__ == "__main__":
    print("To-Do Manager")
    print("-------------")

    while True:
        print("\nOptions:")
        print("1. View todos")
        print("2. Add todo")
        print("3. Remove todo")
        print("4. Search todos")
        print("5. Clear all todos")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            todos = get_todos()
            if not todos:
                print("No todos yet.")
            else:
                for i, todo in enumerate(todos, 1):
                    print(f"{i}. {todo.strip()}")

        elif choice == "2":
            item = input("Enter new todo: ")
            add_todo(item)
            print("Todo added!")

        elif choice == "3":
            index = int(input("Enter todo number to remove: "))
            removed = remove_todo(index)
            if removed:
                print(f"Removed: {removed}")
            else:
                print("Invalid index!")

        elif choice == "4":
            keyword = input("Search keyword: ")
            results = search_todos(keyword)
            if results:
                print("Found:")
                for r in results:
                    print(" -", r)
            else:
                print("No matching todos!")

        elif choice == "5":
            clear_todos()
            print("All todos cleared!")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")
