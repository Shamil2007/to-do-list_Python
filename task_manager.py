from options.add_task import AddTask
from options.remove_task import RemoveTask
from options.view_task import ViewTask


class TaskManager:
    @staticmethod
    def choose_option(option):
        if option == 1:
           AddTask().add_task()
        elif option == 2:
            RemoveTask().remove_task()
        elif option == 3:
            ViewTask().view_tasks()
        else:
            print("Thanks for using this To-Do List App. Happy organizing!")

        return option