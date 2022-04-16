todos = []


class Todo:
    id = 1

    _description = None
    _isDone = False
    _id = None

    def __init__(self, description, isDone):

        self._description = description
        self._isDone = isDone

        self._id = Todo.id
        Todo.id += 1


def Add(description, isDone):
    todos.append(Todo(description=description, isDone=isDone))


def List():
    for todo in todos:
        print("{} {}: {}".format(todo._id, todo._description, todo._isDone))


Add("Hello", True)
Add("World", False)
List()

# Welcome
# Display todos?
# What would you like to do?
#   1. List
#   2. Update
#   3. Add
