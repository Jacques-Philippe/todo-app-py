from copy import copy
from todoapp import TodoApp
from todo import Todo

# Adding a todo should increase the todo list size by one
# The added todo should subsequently be visible, with the expected data


def test_todoadd():
    app = TodoApp()
    initial_length = len(app.todos)
    description = "Hello world"
    isDone = True
    app.Add(description=description, isDone=isDone)
    assert(len(app.todos) == initial_length + 1)
    todo = app.todos[len(app.todos) - 1]
    assert(todo._description == description)
    assert(todo._isDone == isDone)


# Updating a todo should have the expected effect on the todo list state
def test_todoedit():
    app = TodoApp()
    old_description = "Hello world"
    old_is_done = True
    app.Add(description=old_description, isDone=old_is_done)
    old_todo = copy(app.todos[len(app.todos) - 1])
    id = old_todo._id

    app.Update(id, new_description=old_description, new_is_done=old_is_done)
    new_todo = next(todo for todo in app.todos if todo._id == old_todo._id)
    assert(new_todo._description == old_todo._description)
    assert(new_todo._isDone == old_todo._isDone)

    new_description = "Goodbye!"
    new_is_done = False

    app.Update(id, new_description=old_description, new_is_done=new_is_done)
    new_todo = next(todo for todo in app.todos if todo._id == old_todo._id)
    assert(new_todo._description == old_todo._description)
    assert(new_todo._isDone != old_todo._isDone)

    app.Update(id, new_description=new_description, new_is_done=old_is_done)
    new_todo = next(todo for todo in app.todos if todo._id == old_todo._id)
    assert(new_todo._description != old_todo._description)
    assert(new_todo._isDone == old_todo._isDone)

    app.Update(id, new_description=new_description, new_is_done=new_is_done)
    new_todo = next(todo for todo in app.todos if todo._id == old_todo._id)
    assert(new_todo._description != old_todo._description)
    assert(new_todo._isDone != old_todo._isDone)
