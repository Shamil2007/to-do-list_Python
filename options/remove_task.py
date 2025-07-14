import json
import os
from typing import TextIO

from input_handler import InputHandler
from options.view_task import ViewTask


class RemoveTask:
    def __init__(self, filename="lists/to_do.json"):
        self.fileName = filename
        self.handler = InputHandler()

        if not os.path.exists(self.fileName) or os.stat(self.fileName).st_size == 0:
            with open(self.fileName, "w", encoding="UTF-8") as file: # type: TextIO
                json.dump([], file)

    def remove_task(self):
        try:
            with open(self.fileName, "r", encoding="UTF-8") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ No tasks to remove.")
            return

        while True:
            removedTask = self.handler.find_task_handler("remove")

            if isinstance(removedTask, int):
                # Remove by Index
                if not any(task.get("Index") == removedTask for task in tasks):
                    print("\n❗ No task found with that index.\n")
                    continue
                updatedTasks = [task for task in tasks if task.get("Index") != removedTask]
            else:
                # Remove by Task name
                if not any(task.get("Task") == removedTask for task in tasks):
                    print("\n❗ No task found with that name.\n")
                    continue
                updatedTasks = [task for task in tasks if task.get("Task") != removedTask]

            i = 1
            for task in updatedTasks:
                task["Index"] = i
                i += 1

            with open(self.fileName, "w", encoding="UTF-8") as file:  # type: TextIO
                json.dump(updatedTasks, file, indent=3)

            print("✅ Task removed successfully.")
            break
