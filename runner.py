from bookscraper.scrapeBooks import BookScraper
from quotescraper.scrapeQuotes import QuoteScraper
from base.base import Base
from exit.exit import UserExit, ProgramExit
from filemanager.file_ops_menu import start_reading_files
from filemanager.file_ops_menu import start_clearing_files
from constants.constants import BASE_URL, CHROME_AGENTS_URL
import requests
import os
import random

# Important for a vnc server
# os.environ["DISPLAY"] = ":1"


# The main function
def main():
    res = requests.get(CHROME_AGENTS_URL)
    if res.status_code == 200:
        data = res.text
        agents = data.split("\n")
    else:
        print(
            "An error occured with status code: %s\nBut was handled with a fallback"
            % (res.status_code))
        AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3.1 Mobile/15E148 Safari/604.1"
    try:
        scraper = None
        # Base class
        if isinstance(agents, list):
            AGENT = random.choice(agents)

        print(AGENT)

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
