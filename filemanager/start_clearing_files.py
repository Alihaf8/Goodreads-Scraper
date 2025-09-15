from bookscraper.options.clear_csv_file import clear_csv_file
from quotescraper.options.clear_txt_file import clear_txt_file


def start_clearing_files():
    while True:
        print(f"\n{' Clear Files ':=^50}")
        print("\nWhich file do you want to clear?")
        print("*** 1: Books ('books.csv' file)")
        print("*** 2: Quotes ('quotes.txt' file)")
        user_file = input(
            "\nPlease enter an option (1-2) 'E' to cancel: ").strip()

        try:
            user_file = int(user_file)

            if user_file == 1:
                print("=" * 50)
                print()
                print(f"{' CSV file cleared successfully ':^50}")
                return clear_csv_file()
            elif user_file == 2:
                print("=" * 50)
                print()
                print(f"{' TXT file cleared successfully ':^50}")
                return clear_txt_file()
            else:
                print("\nInvalid option !")

        except ValueError:
            if user_file.lower() == 'e':
                return

            else:
                print("\nInvalid Input !")
