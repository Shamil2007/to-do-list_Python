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
              "This sleek and simple To-Do List app is built with Python to help you effortlessly manage your daily chores, goals, and ideas. \n")

        t.sleep(1)
        print("With just a few easy commands, you can:\n"
              " - Add new tasks in a snap ✅\n"
              " - View your task list anytime 👀\n"
              " - Remove completed tasks with ease 🗑️\n")

    @staticmethod
    def print_usage_info():
        import time

        print("\n        ===================================================")
        print("                    📝 PYTHON TO-DO LIST APP")
        print("        ===================================================")
        time.sleep(1)

        print("""
        Welcome to your personal Python-powered To-Do List!

        This is a simple command-line application to help you:
            - Stay organized
            - Track your daily tasks
            - Boost your productivity
        """)
        time.sleep(1)

        print("               -------------------------------------")
        print("                           📌 Features:")
        print("               -------------------------------------")
        print("""\
        1️⃣ Add a Task
            ➤ Add new tasks to your list anytime.

        2️⃣ Remove a Task
            ➤ Delete tasks you've completed.

        3️⃣ View All Tasks
            ➤ See a clean list of your pending tasks.

        4️⃣ Exit
            ➤ Quit the application safely.
        """)
        time.sleep(1)

        print("               -------------------------------------")
        print("                          🔧 How to Use:")
        print("               -------------------------------------")
        print("""\
        - When the app starts, you'll see a menu of options.
        - Simply enter the number of the action you'd like to perform.
        For example:
            ▸ Enter `1` to add a new task.
            ▸ Enter `2` to remove a task by its number.
            ▸ Enter `3` to view all tasks.
            ▸ Enter `4` to exit the program.

        - The app will guide you through each step — no worries!
        """)
        time.sleep(1)

        print("               -------------------------------------")
        print("                         💡 Example Flow:")
        print("               -------------------------------------")
        print("""\
        > What would you like to do?
            > 1. Add Task
            > 2. Remove Task
            > 3. View Tasks
            > 4. Exit

        Enter your choice: 1
        Enter your task: Finish homework

        Task added! ✅
        """)
        time.sleep(1)

        print("        -------------------------------------------------------------")
        print("            Thanks for using this To-Do List App. Happy organizing!")
        print("        -------------------------------------------------------------")
        time.sleep(1)

        print("\n               ========================================")
        print("                             Read me is over")
        print("               ========================================\n")

    @staticmethod
    def menu():
        print("""
> What would you like to do?
    > 1. Add Task
    > 2. Remove Task
    > 3. View Tasks
    > 4. Exit
        """)