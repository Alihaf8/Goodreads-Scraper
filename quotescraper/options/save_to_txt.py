from constants.constants import QUOTE_PATH
import os


def save_to_txt(text):
    for _ in range(10):
        if not os.path.basename(os.getcwd()) == "goodreads":
            os.chdir('..')

    if not os.path.exists(QUOTE_PATH):
        print(
            "Text file or folder not found !\n***Skipping saving operation !")

    else:
        with open(QUOTE_PATH, "a") as f:
            f.write(f"{text}\n\n\n")
