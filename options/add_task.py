import json
import os
from datetime import datetime
from typing import TextIO
from input_handler import InputHandler


class AddTask:
    def __init__(self, fileName="lists/to_do.json"):
        self.fileName = fileName
        self.handler = InputHandler()

        if not os.path.exists(self.fileName) or os.stat(self.fileName).st_size == 0:
            with open(self.fileName, "w", encoding="UTF-8") as file: # type: TextIO
                json.dump([], file)

    def add_task(self):
        newTask = self.handler.add_task_handler()

        try:
            with open(self.fileName, "r", encoding="UTF-8") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            tasks = []

        if tasks:
            max_index = max(task.get("Index", 0) for task in tasks)
            next_index = max_index + 1
        else:
            next_index = 1

        tasks.append({
            "Task": newTask,
            "Add Date": datetime.now().strftime("%Y-%m-%d"),
            "Index": next_index,
            "Done": False,
        })

        with open(self.fileName, "w", encoding="UTF-8") as file: # type: TextIO
            json.dump(tasks, file, indent=5)

        print("✅ Task successfully added")
