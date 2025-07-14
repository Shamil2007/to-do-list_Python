import json
import os
from typing import TextIO

from input_handler import InputHandler


class ModifyTask:
    def __init__(self, fileName="lists/to_do.json"):
        self.fileName = fileName
        self.handler = InputHandler()

        if not os.path.exists(self.fileName) or os.stat(self.fileName).st_size == 0:
            with open(self.fileName, "w", encoding="UTF-8") as file: # type: TextIO
                json.dump([], file)

    def modify_text(self):
        try:
            with open(self.fileName, "r", encoding="UTF-8") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ No tasks to modify.")
            return

        while True:
            task_to_modify = self.handler.find_task_handler("modify", self.fileName)
            if task_to_modify == "Exit":
                print("❌ Modification cancelled.")
                return

            if isinstance(task_to_modify, int):
                if not any(task.get("Index") == task_to_modify for task in tasks):
                    print("\n❗ No task found with that index.\n")
                    continue

                new_name = self.handler.modify_task_handler()

                for task in tasks:
                    if task.get("Index") == task_to_modify:
                        task["Task"] = new_name
                        break

            else:
                if not any(task.get("Task") == task_to_modify for task in tasks):
                    print("\n❗ No task found with that name.\n")
                    continue

                new_name = self.handler.modify_task_handler()

                for task in tasks:
                    if task.get("Task") == task_to_modify:
                        task["Task"] = new_name
                        break

            with open(self.fileName, "w", encoding="UTF-8") as file:  # type: TextIO
                json.dump(tasks, file, indent=3)

            print("✅ Task modified successfully.")
            break
