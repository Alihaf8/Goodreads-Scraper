from constants.constants import QUOTE_PATH
import os


def read_txt_file():
    for _ in range(10):
        if not "goodreads" in os.path.basename(os.getcwd()).lower():
            os.chdir('..')

    if not os.path.exists(QUOTE_PATH):
        print(
            "Text file or folder not found !\n***Skipping reading operation !")

    else:
        with open(QUOTE_PATH, "r") as f:
            content = f.read()
            print(content)
