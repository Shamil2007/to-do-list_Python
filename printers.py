import time
import time as t


class Printers:
    @staticmethod
    def intro_to_list():
        print("""
        ************************************************************
        *                                                          *
        *        WELCOME TO YOUR ULTIMATE PYTHON TO-DO LIST!       *
        *                                                          *
        ************************************************************
        
        """)

        t.sleep(1)
        print("Stay organized, boost your productivity, and never forget a task again! \n"
              "This sleek and simple To-Do List app is built with Python "
              "\n           to help you effortlessly manage your daily chores, goals, and ideas. \n")

        t.sleep(1)
        print("With just a few easy commands, you can:\n"
              " - Add new tasks in a snap ✅\n"
              " - View your task list anytime 👀\n"
              " - Remove completed tasks with ease 🗑️\n")

    @staticmethod
    def print_usage_info():
        import time

        try:
            with open("README.md", "r", encoding="utf-8") as file:
                for line in file:
                    print(line.rstrip())
                    time.sleep(0.03)  # Optional: Typing effect
        except FileNotFoundError:
            print("❗ README.md file not found.")

    @staticmethod
    def menu(fileName):
        time.sleep(0.3)
        print(f"\nActive file: {fileName[6:]}")
        time.sleep(0.3)

        print("""
> What would you like to do?
    > 1. Add Task
    > 2. Remove Task
    > 3. View Tasks
    > 4. Done Tasks
    > 5. Modify Task
    > 6. Change File
    > 7. Exit
        """)