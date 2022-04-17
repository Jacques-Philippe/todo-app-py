import enum
import os
from pydoc import isdata
from prompt_toolkit import print_formatted_text as print, prompt, PromptSession
from prompt_toolkit.validation import ValidationError, Validator
from prompt_toolkit.completion import WordCompleter
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


def Update(id, new_description, new_is_done):
    for index, todo in enumerate(todos):
        if todo._id == id:
            todos[index]._description = new_description
            todos[index]._isDone = new_is_done


def List():
    for todo in todos:
        print("{} {}: {}".format(todo._id, todo._description, todo._isDone))


class MenuChoiceValidator(Validator):
    def validate(self, document):
        text = document.text

        if text and not text.isdigit():
            i = 0

            # Get index of first non numeric character.
            # We want to move the cursor here.
            for i, c in enumerate(text):
                if not c.isdigit():
                    break

            raise ValidationError(
                message='This input contains non-numeric characters', cursor_position=i)
        elif text and text.isdigit() and not int(text) in range(1, 4):
            raise ValidationError(
                message='Input should be between 1 and 3', cursor_position=len(text))
        elif not text:
            raise ValidationError(
                message='Input should contain numeric characters', cursor_position=len(text))


class TodoPickerValidator(Validator):
    def validate(self, document):
        text = document.text

        if text and not text.isdigit():
            i = 0

            # Get index of first non numeric character.
            # We want to move the cursor here.
            for i, c in enumerate(text):
                if not c.isdigit():
                    break

            raise ValidationError(
                message='This input contains non-numeric characters', cursor_position=i)
        elif text and text.isdigit() and not int(text) in range(1, len(todos) + 1):
            raise ValidationError(
                message='Input should be between 1 and {}'.format(len(todos)), cursor_position=len(text))


class YesOrNoValidator(Validator):
    affirmative_options = ["y", "yes", "Y", "Yes"]
    negative_options = ["n", "no", "N", "No"]
    options = affirmative_options + negative_options

    def validate(self, document):
        text = document.text
        if text and not text.lower() in YesOrNoValidator.options:
            raise ValidationError(
                message='Please give a yes or no answer', cursor_position=len(text))


class BoolValidator(Validator):
    affirmative_options = ["t", "true", "T", "True"]
    negative_options = ["f", "false", "F", "False"]
    options = affirmative_options + negative_options

    def validate(self, document):
        text = document.text
        if text and not text.lower() in BoolValidator.options:
            raise ValidationError(
                message='Please say true or false', cursor_position=len(text))


print("Welcome to the todos program!")
MENU_PROMPT = '''
What would you like to do?
1. Add a new todo item.
2. Update an existing todo item.
3. Exit.
'''

DESCRIPTION_PROMPT = '''
What is the item's description?
'''

IS_DONE_PROMPT = '''
Is the item done?
'''

UPDATE_TODO_PROMPT = '''
Please select a todo to update
'''

SHOULD_CHANGE_DESCRIPTION_PROMPT = '''
Change description?
'''

SHOULD_CHANGE_IS_DONE_PROMPT = '''
Change isDone?
'''

CHANGE_DESCRIPTION_PROMPT = '''
What would you like the new description to be?
'''

CHANGE_IS_DONE_PROMPT = '''
What would you like the new isDone to be?
'''


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


input = None

while not input == 3:
    # clearConsole()
    List()
    input = int(prompt(MENU_PROMPT,
                       validator=MenuChoiceValidator()))
    if (input == 1):
        description = prompt(DESCRIPTION_PROMPT)
        isDone = prompt(
            IS_DONE_PROMPT, validator=YesOrNoValidator(), completer=WordCompleter(YesOrNoValidator.options)) in YesOrNoValidator.affirmative_options
        Add(description=description, isDone=isDone)
    elif (input == 2):
        if (len(todos) < 1):
            print("There are no todos to update")
            continue
        id = int(prompt(UPDATE_TODO_PROMPT, validator=TodoPickerValidator(),
                 completer=WordCompleter([str(id) for id in range(1, len(todos) + 1)])))
        todo = todos[id - 1]
        new_description = todo._description
        new_is_done = todo._isDone
        should_change_description = prompt(
            SHOULD_CHANGE_DESCRIPTION_PROMPT, validator=YesOrNoValidator(), completer=WordCompleter(YesOrNoValidator.options)) in YesOrNoValidator.affirmative_options
        if should_change_description:
            new_description = prompt(
                CHANGE_DESCRIPTION_PROMPT, default=todo._description)

        should_change_is_done = prompt(
            SHOULD_CHANGE_IS_DONE_PROMPT, validator=YesOrNoValidator(), completer=WordCompleter(YesOrNoValidator.options)) in YesOrNoValidator.affirmative_options
        if should_change_is_done:
            output = prompt(
                CHANGE_IS_DONE_PROMPT, default=str(todo._isDone), completer=WordCompleter(BoolValidator.options), validator=BoolValidator())
            new_is_done = output in BoolValidator.affirmative_options

        Update(id, new_description=new_description, new_is_done=new_is_done)

print("Program end.")
