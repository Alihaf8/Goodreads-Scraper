from bookscraper.options.read_csv_file import read_csv_file
from quotescraper.options.read_txt_file import read_txt_file


def start_reading_files():
    while True:
        print(f"\n{' Read Files ':=^50}")
        print("\nWhich file do you want to read?")
        print("*** 1: Books ('books.csv' file)")
        print("*** 2: Quotes ('quotes.txt' file)")
        user_file = input("\nPlease enter an option (1-2) 'E' to cancel: ")

        try:
            user_file = int(user_file)

            if user_file == 1:
                print("=" * 50)
                return read_csv_file()
            elif user_file == 2:
                print("=" * 50)
                print("\n\n\n")
                return read_txt_file()
            else:
                print("\nInvalid option !")

        except ValueError:
            if user_file.lower() == 'e':
                return

            else:
                print("\nInvalid Input !")
