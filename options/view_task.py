import json

class ViewTask:
    def __init__(self, fileName="files/to_do.json"):
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
                if data == "Task":
                    print(f"Task is '{task[data]}'")
                elif data == "Date":
                    print(f"The task added in {task[data]}")
                else:
                    print(f"The task number is {task[data]}")
                    print("-" * (max(len(task['Task']), len(task['Date'])) + len("The task added in") + 2))
        return