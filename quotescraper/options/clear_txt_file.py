from constants.constants import QUOTE_PATH
import os


def clear_txt_file():
    for _ in range(10):
        if not os.path.basename(os.getcwd()) == "goodreads":
            os.chdir('..')

    if not os.path.exists(QUOTE_PATH):
        print(
            "Clear text file or folder not found !\n***Skipping clear operation !"
        )

    else:
        with open(QUOTE_PATH, "w") as f:
            f.write("")
