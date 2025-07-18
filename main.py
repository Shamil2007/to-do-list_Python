from printers import Printers
from input_handler import InputHandler
from task_manager import TaskManager


class Main:
    def __init__(self):
        self.printer = Printers()
        self.input_handler = InputHandler()

    def run(self):
        self.printer.intro_to_list()
        self.input_handler.ask_to_show_readme()

        manager = TaskManager()
        while True:
            choice = self.input_handler.ask_for_menu_choice(manager.fileName, 7)
            if manager.choose_option(choice) == 7:
                break


if __name__ == '__main__':
    main = Main()
    main.run()