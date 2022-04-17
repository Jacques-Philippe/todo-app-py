
from prompts import (GetDescription, GetIdToUpdate, GetIsDone, GetMenuChoice, GetNewDescription, GetNewIsDone,
                     GetShouldChangeDescription, GetShouldChangeIsDone)
from todo import Todo


class TodoApp:
    todos = []

    def Add(self, description, isDone):
        self.todos.append(Todo(description=description, isDone=isDone))

    def Update(self, id, new_description, new_is_done):
        for index, todo in enumerate(self.todos):
            if todo._id == id:
                self.todos[index]._description = new_description
                self.todos[index]._isDone = new_is_done

    def DisplayExistingTodos(self):
        for todo in self.todos:
            print("{} {}: {}".format(todo._id, todo._description, todo._isDone))

    def Run(self):
        input = None

        while not input == 3:
            self.DisplayExistingTodos()
            input = GetMenuChoice()

            # Create a new todo
            if (input == 1):
                description = GetDescription()
                isDone = GetIsDone()
                self.Add(description=description, isDone=isDone)

            # Update an existing todo
            elif (input == 2):
                if (len(self.todos) < 1):
                    print("There are no todos to update")
                    continue

                id = GetIdToUpdate(self.todos)
                todo = TodoApp.todos[id - 1]
                new_description = todo._description
                new_is_done = todo._isDone

                should_change_description = GetShouldChangeDescription()
                if should_change_description:
                    new_description = GetNewDescription(todo=todo)

                should_change_is_done = GetShouldChangeIsDone()
                if should_change_is_done:
                    new_is_done = GetNewIsDone(todo=todo)

                self.Update(id, new_description=new_description,
                            new_is_done=new_is_done)
