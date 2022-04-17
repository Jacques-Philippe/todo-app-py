from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


from validators import BoolValidator, MenuChoiceValidator, TodoPickerValidator, YesOrNoValidator


_MENU_PROMPT = '''
What would you like to do?
1. Add a new todo item.
2. Update an existing todo item.
3. Exit.
'''

_DESCRIPTION_PROMPT = '''
What is the item's description?
'''

_IS_DONE_PROMPT = '''
Is the item done?
'''

_UPDATE_TODO_PROMPT = '''
Please select a todo to update
'''

_SHOULD_CHANGE_DESCRIPTION_PROMPT = '''
Change description?
'''

_SHOULD_CHANGE_IS_DONE_PROMPT = '''
Change isDone?
'''

_CHANGE_DESCRIPTION_PROMPT = '''
What would you like the new description to be?
'''

_CHANGE_IS_DONE_PROMPT = '''
What would you like the new isDone to be?
'''


def GetDescription() -> str:
    """
    Gather and return the string to serve as a description for a todo item
    """
    description = prompt(_DESCRIPTION_PROMPT)
    return description


def GetIsDone() -> bool:
    """
    Gather and return the boolean to serve as an isDone value for a todo item
    """
    isDone = prompt(_IS_DONE_PROMPT, validator=YesOrNoValidator(), completer=WordCompleter(
        YesOrNoValidator.options)) in YesOrNoValidator.affirmative_options
    return isDone


def GetIdToUpdate(todos) -> int:
    """
    Gather and return the id used to identify the todo to update
    Note: Assumes ids begin at 1 and end at todos.length
    """
    id = int(prompt(_UPDATE_TODO_PROMPT, validator=TodoPickerValidator(todos=todos),
                    completer=WordCompleter([str(id) for id in range(1, len(todos) + 1)])))
    return id


def GetMenuChoice() -> int:
    """
    Gather and return the menu choice the user makes to drive the app
    """
    input = int(prompt(_MENU_PROMPT,
                       validator=MenuChoiceValidator()))
    return input


def GetShouldChangeDescription() -> bool:
    """
    Gather and return whether the user wishes to change the description of the todo item
    """
    should_change_description = prompt(
        _SHOULD_CHANGE_DESCRIPTION_PROMPT, validator=YesOrNoValidator(), completer=WordCompleter(YesOrNoValidator.options)) in YesOrNoValidator.affirmative_options
    return should_change_description


def GetNewDescription(todo) -> str:
    """
    Gather and return the newer description of the todo item
    """
    new_description = prompt(
        _CHANGE_DESCRIPTION_PROMPT, default=todo._description)
    return new_description


def GetShouldChangeIsDone() -> bool:
    """
    Gather and return whether the user wishes to change the isDone of the todo item
    """
    should_change_is_done = prompt(
        _SHOULD_CHANGE_IS_DONE_PROMPT, validator=YesOrNoValidator(), completer=WordCompleter(YesOrNoValidator.options)) in YesOrNoValidator.affirmative_options
    return should_change_is_done


def GetNewIsDone(todo) -> bool:
    """
    Gather and return the newer isDone of the todo item
    """
    output = prompt(
        _CHANGE_IS_DONE_PROMPT, default=str(todo._isDone), completer=WordCompleter(BoolValidator.options), validator=BoolValidator())
    return output in BoolValidator.affirmative_options
