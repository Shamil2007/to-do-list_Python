import json
import os
from typing import TextIO
from datetime import datetime
from input_handler import InputHandler


class DoneTask:
    def __init__(self, filename="lists/to_do.json"):
        self.fileName = filename
        self.handler = InputHandler()

        if not os.path.exists(self.fileName) or os.stat(self.fileName).st_size == 0:
            with open(self.fileName, "w", encoding="UTF-8") as file: # type: TextIO
                json.dump([], file)

    def done_task(self):
        try:
            with open(self.fileName, "r", encoding="UTF-8") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ No tasks to done.")
            return

        while True:
            doneTask = self.handler.find_task_handler("done", self.fileName)
            if doneTask == "Exit":
                print("❌ Modification cancelled.")
                return

            if isinstance(doneTask, int):
                if not any(task.get("Index") == doneTask for task in tasks):
                    print("\n❗ No task found with that index.\n")
                    continue

                for task in tasks:
                    if task.get("Index") == doneTask:
                        task["Done"] = True
                        task["Finish Date"] = datetime.now().strftime("%Y-%m-%d")
                        break

            else:
                if not any(task.get("Task") == doneTask for task in tasks):
                    print("\n❗ No task found with that name.\n")
                    continue

                for task in tasks:
                    if task.get("Task") == doneTask:
                        task["Done"] = True
                        break

            with open(self.fileName, "w", encoding="UTF-8") as file:  # type: TextIO
                json.dump(tasks, file, indent=5)

            print("✅ Task modified successfully.")
            break