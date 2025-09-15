from bookscraper.scrapeBooks import BookScraper
from quotescraper.scrapeQuotes import QuoteScraper
from base.base import Base
from exit.exit import UserExit, ProgramExit
from filemanager.start_reading_files import start_reading_files
from filemanager.start_clearing_files import start_clearing_files
from constants.constants import BASE_URL
import os
import random

# Important for a vnc server
os.environ["DISPLAY"] = ":1"

# Agent can be changed
AGENT = "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36"


# The main function
def main():
    try:
        scraper = ""
        # Base class
        base = Base(BASE_URL, AGENT)

        while True:
            user_in = base.get_user_choice()
            if user_in == 1:
                # Scrape Books
                scraper = BookScraper(BASE_URL, AGENT)

            elif user_in == 2:
                # Scrape Quotes
                scraper = QuoteScraper(BASE_URL + "/quotes", AGENT)

            elif user_in == 3:
                # Read files
                start_reading_files()
                continue

            else:
                # Clear files
                start_clearing_files()
                continue

        exiting(scraper)
    except (UserExit, ProgramExit):
        pass

    except KeyboardInterrupt:
        print(f"\n{' EXITED ':-^50}")


def exiting(scraper):
    input("Press ENTER to exit...")
    scraper.driver.quit()


if __name__ == "__main__":
    main()
