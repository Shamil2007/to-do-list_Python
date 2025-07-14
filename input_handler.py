import os

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

    def ask_for_menu_choice(self, fileName):
        value_range = [1, 6]
        while True:
            self.printer.menu(fileName)
            try:
                choice = int(input("Please enter a number (1–6): ").strip())
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")
                continue

            if not self.check_range(choice, value_range):
                continue
            return choice

    @staticmethod
    def add_task_handler():
        while True:
            task = input("Enter your task: ")
            isTaskCorrectFormation = ErrorChecker.check_taskName(task)
            if isTaskCorrectFormation:
                return task

    @staticmethod
    def find_task_handler(type_of_task):
        print(f"\nWhich task do you want to {type_of_task}? ")

        task = input("Enter either index or task name: ")
        try:
            taskNumber = int(task)
            return taskNumber
        except ValueError:
            return task

    @staticmethod
    def modify_task_handler():
        while True:
            newTaskName = input("What is the new name of the task? ")
            isTaskCorrectFormation = ErrorChecker.check_taskName(newTaskName)
            if isTaskCorrectFormation:
                return newTaskName

    @staticmethod
    def set_file_name(folder):
        while True:
            name = input("Enter the file name (e.g., todo.json): ").strip()
            if ErrorChecker.is_valid_filename(name):
                full_path = os.path.join(folder, name)
                if os.path.exists(full_path):
                    print("A file with this name already exists.")
                    overwrite = input("Do you want to overwrite it? (y/n): ").lower()
                    if overwrite != 'y':
                        return "No override", full_path
                return '_', full_path