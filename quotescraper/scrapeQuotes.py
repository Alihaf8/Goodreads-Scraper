from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
from exit.exit import UserExit, ProgramExit
from bs4 import BeautifulSoup
from base.base import Base
from quotescraper.options.save_to_txt import save_to_txt
from quotescraper.options.clear_txt_file import clear_txt_file
from quotescraper.options.read_txt_file import read_txt_file


class QuoteScraper(Base):

    def __init__(self, url, user_agent):
        super().__init__(url, user_agent)
        self.url = url
        self.quotes = None
        self.launch_page()
        self.search_quotes()

    def user_search_quote(self):
        while True:
            user_query = input(
                "\nEnter a quote subject (e.g. [Love, Life, Wisdom, etc...] or 'E' to EXIT): "
            ).strip()

            if user_query == "":
                print("\nPlease enter a valid, quote subject !")
            elif user_query.lower() == "e":
                raise UserExit("User requested exit.")
            else:
                return user_query

    def search_quotes(self):
        self.close_popup()
        self.driver.get(f"{self.url}/search?q={self.user_search_quote()}")
        self.get_all_quotes(1)

    def get_all_quotes(self, page):
        current_url = self.driver.current_url
        self.driver.get(current_url + "&page=" + str(page))
        soup = self.soup(self.driver.page_source)

        self.quotes = soup.find_all("div", class_="quoteText")

        if not self.quotes == []:
            text = f"FOUND {len(self.quotes)} RESULTS IN PAGE {page}"
            print()
            print("=" * 50)
            print(f"{text:^50}")
            print("=" * 50)
            if len(self.quotes) > 1:
                for i, quote in enumerate(self.quotes, start=1):
                    print(f"{i}:\n\t{quote.text.strip()}")
                    print()

            else:
                print(f"\n\t{quote.text.strip()}")

            print("=" * 50)

        else:
            print(f"\n\n\t{'No Results Found !':*>30}")
            self.launch_page()
            return self.search_quotes()

        self.ask_user_for_quote_action()

    def ask_user_for_quote_action(self):
        while True:
            print()
            print("=" * 50)
            print("\nWhat would you like to do next?")
            print("*** 1: Load the next page of results")
            print("*** 2: Search Again")
            print("*** 3: Return to the main menu")
            print("*** 4: Save a specified quote to 'quotes.txt' file")
            print("*** 5: Save quotes to 'quotes.txt' file")
            print("*** 6: Exit the program")
            user_choice = input("\nPlease choose an option (1-6): ").strip()

            try:
                user_choice = int(user_choice)
                if user_choice == 1:
                    return self.get_all_quotes(self.get_quotes_next_page())
                elif user_choice == 2:
                    self.launch_page()
                    return self.search_quotes()
                elif user_choice == 3:
                    return None
                elif user_choice == 4:
                    self.save_specified_quote()
                    continue
                elif user_choice == 5:
                    quotes_txt = []
                    for quote in self.quotes:
                        quotes_txt.append(quote.text)
                    save_to_txt("\n".join(quotes_txt))

                    print(f"\n{'Quotes Saved Successfully !':*>30}")
                    continue
                elif user_choice == 6:
                    raise ProgramExit(
                        "Exiting program. Thank you for using the scraper!")
                else:
                    print(
                        "Invalid choice. Please enter a number between 1 and 6."
                    )

            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_quotes_next_page(self):
        """Prompts the user for a page number to navigate to and validates the input."""
        while True:
            user_input = input(
                "\nEnter a page number (1-100) to view, or 'E' to return to the menu: "
            ).strip()

            try:
                page_num = int(user_input)
                if 1 <= page_num <= 100:
                    return page_num
                else:
                    print("Page number must be between 1 and 100.")

            except ValueError:
                if user_input.lower() == "e":
                    self.ask_user_for_quote_action()
                    return None
                else:
                    print("Please enter a valid number or 'E'.")

    def save_specified_quote(self):
        while True:
            user_index = input(
                f"\nEnter the quote index (number) from the list above (1-{len(self.quotes)}), or 'E' to get back to the menu: "
            )

            try:
                user_index = int(user_index)
                if user_index <= len(self.quotes):
                    print(f"\n{' Quote Saved Successfully ':*^30}")
                    return save_to_txt(self.quotes[user_index - 1].text)
                else:
                    print(
                        f"\n\tPlease, enter a number between (1-{len(self.quotes)})"
                    )

            except ValueError:
                if user_index.lower() == 'e':
                    return None
                else:
                    print("\n\tInvalid Input !")
