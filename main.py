from prompt_toolkit import print_formatted_text as print
from todoapp import TodoApp

if __name__ == "__main__":

    print("Welcome to the todos program!")

    app = TodoApp()
    app.Run()

    print("Program end.")
