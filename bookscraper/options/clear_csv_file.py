from constants.constants import CSV_PATH
import os, csv


def clear_csv_file():
    for _ in range(10):
        if not "goodreads" in os.path.basename(os.getcwd()).lower():
            os.chdir('..')

    if not os.path.exists(CSV_PATH):
        print("The CSV file or directory not found !")

    else:
        header = [
            "Title", "Author(s)", "Ratings", "Genre(s)", "Publish", "Page",
            "Language", "Description"
        ]
        with open(CSV_PATH, "w", newline="") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(header)
