import os

from input_handler import InputHandler


class ChangeFile:
    def __init__(self, fileName="lists/to_do.json"):
        self.fileName = fileName
        self.handler = InputHandler()

    def change_file(self):
        directory = "lists"

        filesArr = []
        for root, dirs, files in os.walk(directory):
            filesArr = files

        print("\nAvailable files: ")
        fileCounter = 1
        for fileName in filesArr:
            print(f"   > {fileCounter}. {fileName}")
            fileCounter += 1

        print("\nWhich file do you want to choose? (if you want to create new file JUST WRITE NEW FILE NAME! ) ")
        checkOverRide, newFilePath = self.handler.set_file_name(directory)
        if checkOverRide != "No override":
            with open(newFilePath, 'w', encoding='utf-8') as f:
                f.write("")
        return newFilePath