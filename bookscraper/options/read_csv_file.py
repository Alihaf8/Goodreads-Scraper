from constants.constants import CSV_PATH
import os, csv


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
