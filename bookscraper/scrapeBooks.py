from base.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
from exit.exit import UserExit, ProgramExit
from bs4 import BeautifulSoup
from filemanager.file_ops import save_to_csv, save_to_json


class BookScraper(Base):

    def __init__(self, url, user_agent):
        super().__init__(url, user_agent)
        self.url = url
        self.books = []
        self.search()

    def search(self):
        query = self.user_search_query()
        if query is None:
            return self.ask_user_for_actions()

        print(f"\nSearching for '{query}', Please wait...")
        self.driver.get(f"{self.url}/search?q={query}")
        self.close_popup()
        self.get_all_books(1)

    def user_search_query(self):
        """Prompts the user for a search query and handles exit requests."""
        while True:
            user_query = input(
                "\nEnter a book title to search (or 'E' to cancel): ").strip()

            if user_query == "":
                print("Please enter a search term.")
                continue
            elif user_query.lower() == "e":
                return None
            else:
                return user_query

    def get_all_books(self, page_number):
        """
        Fetches and displays the list of books from the search results page.
        """
        if page_number is None:
            return self.ask_user_for_actions()
        current_url = self.driver.current_url
        self.driver.get(current_url + f"&page={page_number}")

        page_soup = self.soup(self.driver.page_source)

        # Check if the search returned no results
        no_results_element = page_soup.find("h3",
                                            class_="searchSubNavContainer")
        if no_results_element and "No results" in no_results_element.text:
            print("No results found for your query. Please try again.")
            return
        else:
            # Find all book title elements on the page
            self.books = []
            try:
                self.books = self.wait.until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, "a[class='bookTitle']")))

            except:
                try:
                    books_cite = self.wait.until(
                        EC.presence_of_all_elements_located(
                            (By.CSS_SELECTOR, "cite[class='bookTitle']")))
                    for book in books_cite:
                        self.books.append(book.find_element(By.XPATH, "./a"))

                except Exception as e:
                    print(
                        "\nNo books were found ! Try changing user agent.\nError message: %s"
                        % str(e))
                    return

            text = f"FOUND {len(self.books)} BOOKS ON PAGE {page_number}"

            print(f"\n{'='*50}")
            print(f"{text:^50}")
            print(f"{'='*50}")
            print("\n")
            # Enumerate and print each book title
            for index, book in enumerate(self.books):
                print(f"{index+1}: {book.text.strip()}")
                print()

        self.ask_user_for_actions()

    def ask_user_for_actions(self):
        """Presents the main menu of actions to the user after displaying results."""
        while True:
            print()
            print("=" * 50)
            print("\nWhat would you like to do next?")
            print("*** 1: View details of a book")
            print("*** 2: Load the next page of results")
            print("*** 3: Search Again")
            print("*** 4: Return to the main menu")
            print("*** 5: Save a specified book")
            print("*** 6: Exit the program")
            user_choice = input("\nPlease choose an option (1-6): ").strip()

            try:
                user_choice = int(user_choice)
                if user_choice == 1:
                    return self.get_book_details()
                elif user_choice == 2:
                    return self.get_all_books(self.get_next_page_number())
                elif user_choice == 3:
                    return self.search()
                elif user_choice == 4:
                    return
                elif user_choice == 5:
                    self.user_save_choice()
                    continue
                elif user_choice == 6:
                    raise ProgramExit(
                        "Exiting program. Thank you for using the scraper!")
                else:
                    print(
                        "Invalid choice. Please enter a number between 1 and 6."
                    )

            except ValueError:
                print("Invalid choice. Please enter a number between 1 and 6.")

    def user_save_choice(self):
        while True:
            print("\nChoose a file to save book info:")
            print("*** 1: CSV ('books.csv' file)")
            print("*** 2: JSON ('books.json' file)")
            user_choice = input(
                "\nPlease enter an option (1-2), 'E' to cancel: ").strip()

            try:
                user_choice = int(user_choice)
                book_index = self.get_user_book_index()
                if book_index is None:
                    continue

                else:
                    selected_book = self.books[book_index]
                    book_title = selected_book.text.strip()
                    self.actions.move_to_element(selected_book).pause(
                        random.uniform(0.1, 0.3)).click().perform()
                    self.implicitly_wait(10)
                    book_info = self.book_info(book_title)
                    if user_choice == 1:
                        save_to_csv(book_info)
                        print("=" * 50)
                        print()
                        print(f"{' Book saved in CSV file successfully ':^50}")
                        return
                    elif user_choice == 2:
                        save_to_json(book_info)
                        print("=" * 50)
                        print()
                        print(
                            f"{' Book saved in JSON file successfully ':^50}")
                        return
                    else:
                        print(
                            "\nInvalid option. Please enter an option between (1-2)."
                        )

            except ValueError:
                if str(user_choice).lower() == "e":
                    return
                else:
                    print(
                        "\nInvalid input. Please enter an option between (1-2)."
                    )

    def get_next_page_number(self):
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
                    return None
                else:
                    print("Please enter a valid number or 'E'.")

    def authors(self, soup):
        """Extracts the author(s) from the book page's BeautifulSoup object."""
        author_elements = soup.select("a.ContributorLink[href*='/author/']")

        author_names = set()
        for author in author_elements:
            author_names.add(author.text.strip())

        uni_author_names = list(author_names)
        if uni_author_names:
            return "; ".join(author_names)
        else:
            return "Not available"

    def ratings(self, soup):
        """Extracts the average rating from the book page."""
        return soup.find("div", class_="RatingStatistics__rating").text

    def genres(self, soup):
        genre_text = []
        try:
            # Find and click the "Show more" button for genres
            show_more_button = self.driver.find_elements(
                By.CSS_SELECTOR,
                "button[aria-label='Show all items in the list']")
            self.driver.execute_script("arguments[0].click();",
                                       show_more_button[0])

            genre_elements = soup.find_all(
                "span", class_="BookPageMetadataSection__genreButton")

            for genre in genre_elements:
                genre_text.append(genre.text)

            return "; ".join(genre_text)

        except Exception as e:
            print(f"Error expanding genres: {e}")
            raise ProgramExit("A critical error occurred. Exiting...")

    def publishing(self, soup):
        return soup.find("p", attrs={"data-testid": "publicationInfo"}).text

    def pages(self, soup):
        return soup.find("p", attrs={"data-testid": "pagesFormat"}).text

    def language(self, soup):
        """Navigates to the 'Details' section and extracts the book's language."""
        try:
            details_button = self.driver.find_element(
                By.CSS_SELECTOR,
                "button[aria-label='Book details and editions']")

            self.driver.execute_script("arguments[0].click();", details_button)

            language_element = self.wait.until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//dt[contains(text(), 'Language')]/following-sibling::*[1]"
                )))
            return language_element.text

        except:
            return "Not Available"

    def characters(self, soup):
        try:
            character_elements = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "a[href*='/characters/']")))
            character_names = [
                character.text for character in character_elements
            ]

            if character_names:
                return "; ".join(character_names)

        except Exception as e:
            return "Not Available"

    def description(self, soup):
        return soup.find(
            "div", class_="DetailsLayoutRightParagraph__widthConstrained").text

    def book_info(self, book_title):
        book_soup = self.soup(self.driver.page_source)
        return {
            "Title": book_title,
            "Author(s)": self.authors(book_soup),
            "Ratings": self.ratings(book_soup),
            "Genre(s)": self.genres(book_soup),
            "Published": self.publishing(book_soup),
            "Pages": self.pages(book_soup),
            "Language": self.language(book_soup),
            "Character(s)": self.characters(book_soup),
            "Description": self.description(book_soup),
        }

    def get_book_details(self):
        user_index = self.get_user_book_index()
        if user_index is None:
            return self.ask_user_for_actions()

        selected_book = self.books[user_index]
        book_title = selected_book.text.strip()

        print(f"\nOpening '{book_title}'...")
        self.actions.move_to_element(selected_book).pause(
            random.uniform(0.1, 0.3)).click().perform()

        self.driver.implicitly_wait(10)

        # Display the compiled book info in a formatted way
        print(f"\n{' BOOK DETAILS ':=^50}")

        for key, value in self.book_info(book_title).items():
            print(f"\n{key:>12}: {value}")

        print(f"\n{' Saved Book To \'books.csv\' Successfully ':*^30}")

        # Return to search after viewing details
        return

    def get_user_book_index(self):
        """Prompts the user to select a book from the list and validates the input."""
        while True:
            user_input = input(
                f"\nEnter the number of the book (1-{len(self.books)}), or 'E' to cancel: "
            ).strip()

            try:
                index = int(user_input)
                if 1 <= index <= len(self.books):
                    return index - 1  # Convert to zero-based index
                else:
                    print(
                        f"Please enter a number between 1 and {len(self.books)}."
                    )

            except ValueError:
                if str(user_input).lower() == "e":
                    return
                else:
                    print("Invalid input. Please enter a number or 'E'.")
