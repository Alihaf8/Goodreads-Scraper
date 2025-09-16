from constants.constants import QUOTE_PATH, CSV_PATH, JSON_PATH
import os, csv
import json


# Save books to a csv file
def save_to_csv(info):
    for _ in range(10):
        if not "goodreads" in os.path.basename(os.getcwd()).lower():
            os.chdir('..')

    if not os.path.exists(CSV_PATH):
        print(
            "The CSV file or directory not found !\n *** Skipping saving operation !"
        )

    else:
        with open(CSV_PATH, "a", newline="") as f:
            csv_writer = csv.writer(f)

            info_arr = []
            for value in info.values():
                info_arr.append(value)

            csv_writer.writerow(info_arr)


def clear_csv_file():
    for _ in range(10):
        if not "goodreads" in os.path.basename(os.getcwd()).lower():
            os.chdir('..')

    if not os.path.exists(CSV_PATH):
        print(
            "The CSV file or directory not found !\n*** Skipping clear operation !"
        )

    else:
        header = [
            "Title", "Author(s)", "Ratings", "Genre(s)", "Publish", "Page",
            "Language", "Character(s)", "Description"
        ]
        with open(CSV_PATH, "w", newline="") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(header)


def read_csv_file():
    for _ in range(10):
        if not "goodreads" in os.path.basename(os.getcwd()).lower():
            os.chdir('..')

    if not os.path.exists(CSV_PATH):
        print(
            "The CSV file or directory not found ! \n*** Skipping reading operation !"
        )

    else:
        with open(CSV_PATH, "r", newline="") as f:
            csv_reader = csv.reader(f)
            next(csv_reader, None)
            print()
            for row in csv_reader:
                if row:
                    print("\n\n\n")
                    print(f"\n\tTitle: {row[0]}")
                    print(f"\n\tAuthor(s): {row[1]}")
                    print(f"\n\tRatings: {row[2]}")
                    print(f"\n\tGenre(s): {row[3]}")
                    print(f"\n\tPublish: {row[4]}")
                    print(f"\n\tPages: {row[5]}")
                    print(f"\n\tLanguage: {row[6]}")
                    print(f"\n\rCharacter(s): {row[7]}")
                    print(f"\n\n\tDescription: {row[8]}")
                    print("\n\n\n")

                else:
                    print("File empty !")


# Save quotes to txt file
def save_to_txt(text):
    for _ in range(10):
        if not "goodreads" in os.path.basename(os.getcwd()).lower():
            os.chdir('..')

    if not os.path.exists(QUOTE_PATH):
        print(
            "Text file or folder not found !\n*** Skipping saving operation !")

    else:
        with open(QUOTE_PATH, "a") as f:
            f.write(f"{text}\n\n\n")


def clear_txt_file():
    for _ in range(10):
        if not "goodreads" in os.path.basename(os.getcwd()).lower():
            os.chdir('..')

    if not os.path.exists(QUOTE_PATH):
        print(
            "Clear text file or folder not found !\n*** Skipping clear operation !"
        )

    else:
        with open(QUOTE_PATH, "w") as f:
            f.write("")


def read_txt_file():
    for _ in range(10):
        if not "goodreads" in os.path.basename(os.getcwd()).lower():
            os.chdir('..')

    if not os.path.exists(QUOTE_PATH):
        print(
            "Text file or folder not found !\n*** Skipping reading operation !"
        )

    else:
        with open(QUOTE_PATH, "r") as f:
            content = f.read()
            print(content)


# Save books to a json file
def save_to_json(info):
    for _ in range(10):
        if not "goodreads" in os.path.basename(os.getcwd()).lower():
            os.chdir("..")

    if not os.path.exists(JSON_PATH):
        print(
            "JSON file or folder not found !\n*** Skipping saving operation !")

    else:
        with open(JSON_PATH, "a", newline="") as f:
            json.dump(info, f)


def clear_json_file():
    for _ in range(10):
        if not "goodreads" in os.path.basename(os.getcwd()).lower():
            os.chdir("..")

    if not os.path.exists(JSON_PATH):
        print(
            "JSON file or folder not found !\n*** Skipping clearing operation !"
        )

    else:
        with open(JSON_PATH, "w", newline="") as f:
            f.write("")


def read_json_file():
    for _ in range(10):
        if not "goodreads" in os.path.basename(os.getcwd()).lower():
            os.chdir("..")

    if not os.path.exists(JSON_PATH):
        print(
            "JSON file or folder not found !\n*** Skipping reading operation !"
        )

    else:
        with open(JSON_PATH, "r", newline="") as f:
            content = json.load(f)
            print("\n\n")
            for key, value in content.items():
                print(f"{key}: {value}\n\n")
