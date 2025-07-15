from options.add_task import AddTask
from options.change_file import ChangeFile
from options.done_task import DoneTask
from options.modify_task import ModifyTask
from options.remove_task import RemoveTask
from options.view_task import ViewTask


class TaskManager:
    def __init__(self):
        self.fileName = "lists/to_do.json"

    def choose_option(self, option):
        if option == 1:
           AddTask(self.fileName).add_task()
        elif option == 2:
            RemoveTask(self.fileName).remove_task()
        elif option == 3:
            ViewTask(self.fileName).view_tasks()
        elif option == 4:
            DoneTask(self.fileName).done_task()
        elif option == 5:
            ModifyTask(self.fileName).modify_text()
        elif option == 6:
            self.fileName = ChangeFile().change_file()
            print(f"File changed to: {self.fileName}")
        else:
            print("Thanks for using this To-Do List App. Happy organizing!")

        return option