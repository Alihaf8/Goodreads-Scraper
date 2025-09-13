from constants.constants import CSV_PATH
import os, csv


def save_to_csv(info):
    for _ in range(10):
        if not "goodreads" in os.path.basename(os.getcwd()).lower():
            os.chdir('..')

    if not os.path.exists(CSV_PATH):
        print("The CSV file or directory not found !")

    else:
        with open(CSV_PATH, "a", newline="") as f:
            csv_writer = csv.writer(f)

            info_arr = []
            for value in info.values():
                info_arr.append(value)

            csv_writer.writerow(info_arr)
