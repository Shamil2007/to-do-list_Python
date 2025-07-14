from error_checker import ErrorChecker
from printers import Printers

class InputHandler(ErrorChecker):
    def __init__(self):
        self.printer = Printers()
        self._first_time = True

    @staticmethod
    def get_boolean_input():
        while True:
            user_input = input("Enter a value ('1', '0', 'True', 'False', 'yes', 'no', 'y', 'n'): ").strip().lower()
            check_boolean_correction = ErrorChecker.check_boolean_input(user_input)
            if check_boolean_correction == 'Incorrect Format':
                continue
            return check_boolean_correction

    def ask_to_show_readme(self):
        if self._first_time:
            print("Would you like to view the README?")
            if self.get_boolean_input():
                self.printer.print_usage_info()
            self._first_time = False

    def ask_for_menu_choice(self):
        value_range = [1, 4]
        while True:
            self.printer.menu()
            try:
                choice = int(input("Please enter a number (1–4): ").strip())
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
                continue

            if not self.check_range(choice, value_range):
                continue
            return choice

    @staticmethod
    def add_task_handler():
        while True:
            task = input("Enter your task: ")
            isTaskCorrectFormation = ErrorChecker.check_addTask(task)
            if isTaskCorrectFormation:
                return task

    @staticmethod
    def remove_task_handler():
        print("\nWhich task do you want to remove? ")

        task = input("Enter either index or task name: ")
        try:
            taskNumber = int(task)
            return taskNumber
        except ValueError:
            return task