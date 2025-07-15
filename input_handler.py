import os

from error_checker import ErrorChecker
from options.view_task import ViewTask
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

    def ask_for_menu_choice(self, fileName, maxRange):
        value_range = [1, maxRange]
        while True:
            self.printer.menu(fileName)
            try:
                choice = int(input(f"Please enter a number (1–{maxRange}): ").strip())
            except ValueError:
                print(f"Invalid input. Please enter a number between 1 and {maxRange}.")
                continue

            if not self.check_range(choice, value_range):
                continue
            return choice

    @staticmethod
    def add_task_handler(fileName):
        while True:
            task = input("Enter your task (Type '!' to view all tasks or 'exit' to cancel):")

            option = ErrorChecker.check_task_handler_options(task)
            if option != False:
                if option == "View":
                    ViewTask(fileName).view_tasks()
                    continue
                elif option == "Exit":
                    return option

            isTaskCorrectFormation = ErrorChecker.check_taskName(task)
            if isTaskCorrectFormation:
                return task

    @staticmethod
    def check_task_availability(taskArr, newTask):
        for task in taskArr:
            if task["Task"] == newTask:
                return True
        return False

    @staticmethod
    def find_task_handler(type_of_task, fileName):
        while True:
            print(f"\nWhich task do you want to {type_of_task}? (Type '!' to view all tasks or 'exit' to cancel)")
            task = input("Enter either index or task name: ").strip()

            checkOption = ErrorChecker.check_task_handler_options(task)

            if checkOption == "View":
                ViewTask(fileName).view_tasks()
                continue
            elif checkOption == "Exit":
                return checkOption

            if task.isdigit():
                return int(task)
            else:
                return task

    @staticmethod
    def modify_task_handler():
        while True:
            newTaskName = input("What is the new name of the task? ")
            isTaskCorrectFormation = ErrorChecker.check_taskName(newTaskName)
            if isTaskCorrectFormation:
                return newTaskName

    @staticmethod
    def set_file_name(folder, filesArr):
        while True:
            name = input("Enter the file name (e.g., todo.json) or choose available file index: ").strip()
            try:
                index = int(name) - 1
                if isinstance(index, int):
                    if not ErrorChecker.check_filesArr(filesArr, index):
                        print("❗ The file index is not available! ")
                        continue
                    fileName = filesArr[index]
                    full_path = os.path.join(folder, fileName)
                    return "No override", full_path
                else:
                    raise ValueError
            except ValueError:
                if ErrorChecker.is_valid_filename(name):
                    full_path = os.path.join(folder, name)
                    if os.path.exists(full_path):
                        print("A file with this name already exists.")
                        overwrite = input("⚠️ Do you want to overwrite it? (y/n): ").lower()
                        if overwrite != 'y':
                            return "No override", full_path
                    return '_', full_path