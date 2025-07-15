import json
import time


class ViewTask:
    def __init__(self, fileName="lists/to_do.json"):
        self.fileName = fileName

    def view_tasks(self):
        try:
            with open(self.fileName, "r", encoding="UTF-8") as file:
                tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ There is no any task in the list! ")
            return

        for task in tasks:
            for data in task:
                time.sleep(0.3)
                if data == "Task":
                    print(f"\nTask is '{task[data]}'")
                elif data == "Date":
                    print(f"The task added in {task[data]}")
                elif data == "Index":
                    print(f"The task number is {task[data]}")
                elif data == "Done":
                    print(f"The task status is {task[data]}")
                else:
                    if task["Done"]:
                        print(f"The task is finished in {task["Finish Date"]}")
            if len(tasks) != 1:
                print("-" * (len(task['Add Date']) + len("The task added in") + 2))
        return