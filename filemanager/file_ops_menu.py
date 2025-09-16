from filemanager.file_ops import clear_csv_file, read_csv_file
from filemanager.file_ops import clear_txt_file, read_txt_file
from filemanager.file_ops import clear_json_file, read_json_file


def start_clearing_files():
    while True:
        print(f"\n{' Clear Files ':=^50}")
        print("\nWhich file do you want to clear?")
        print("*** 1: Books ('books.csv' file)")
        print("*** 2: Books ('books.json' file)")
        print("*** 3: Quotes ('quotes.txt' file)")
        user_file = input(
            "\nPlease enter an option (1-3) 'E' to cancel: ").strip()

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
                print(f"{' JSON file cleared successfully ':^50}")
                return clear_json_file()
            elif user_file == 3:
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
                print("\nInvalid Input. Please enter an option between (1-3).")


def start_reading_files():
    while True:
        print(f"\n{' Read Files ':=^50}")
        print("\nWhich file do you want to read?")
        print("*** 1: Books ('books.csv' file)")
        print("*** 2: Books ('books.json' file)")
        print("*** 3: Quotes ('quotes.txt' file)")
        user_file = input(
            "\nPlease enter an option (1-3) 'E' to cancel: ").strip()

        try:
            user_file = int(user_file)

            if user_file == 1:
                print("=" * 50)
                return read_csv_file()
            elif user_file == 2:
                print("=" * 50)
                try:
                    read_json_file()
                except Exception as e:
                    print(f"An error occureded in json file: {str(e)}")
                finally:
                    return
            elif user_file == 3:
                print("=" * 50)
                print("\n\n\n")
                read_txt_file()
            else:
                print("\nInvalid option !")

        except ValueError:
            if str(user_file).lower() == 'e':
                return

            else:
                print("\nInvalid Input. Please enter an option between (1-3).")
