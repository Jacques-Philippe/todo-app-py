
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
