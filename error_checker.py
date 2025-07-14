import re


class ErrorChecker:
    @staticmethod
    def check_boolean_input(user_input):
        if user_input in ['1', 'true', 'yes', 'y']:
            return 1
        elif user_input in ['0', 'false', 'no', 'n']:
            return 0
        else:
            print("❗ Invalid input. Please enter one of the following: '1', '0', 'True', 'False', 'yes', 'no'.")
            return 'Incorrect Format'

    @staticmethod
    def check_range(value, value_range):
        if not isinstance(value, int):
            return False

        if value_range[0] <= value <= value_range[1]:
            return True

        print(f"❗ The number must be between {value_range[0]} and {value_range[1]}.")
        return False

    @staticmethod
    def check_taskName(task):
        task = task.strip()

        if len(task) == 0:
            print("❗ The task name cannot be empty!")
            return False

        elif len(task) <= 3:
            print("❗ Please be more specific: at least 4 characters!")
            return False

        elif any(char in task for char in ['#', '@', '$', '%', '^', '&', '*']):
            print("⚠️ Avoid using special characters like #, @, $, etc.")
            return False

        elif len(task) > 100:
            print("⚠️ Task name is too long — keep it under 100 characters.")
            return False

        return True

    @staticmethod
    def is_valid_filename(name):
        if not name.strip():
            print("Filename cannot be empty.")
            return False
        if re.search(r'[<>:"/\\|?*]', name):
            print("Filename contains invalid characters.")
            return False
        if not name.endswith(".json"):
            print("Filename must end with .json.")
            return False
        return True