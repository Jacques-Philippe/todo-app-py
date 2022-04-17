from prompt_toolkit.validation import ValidationError, Validator


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
    todos = []

    def __init__(self, todos) -> None:
        super().__init__()
        self.todos = todos

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
        elif text and text.isdigit() and not int(text) in range(1, len(self.todos) + 1):
            raise ValidationError(
                message='Input should be between 1 and {}'.format(len(self.todos)), cursor_position=len(text))


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
