from bookscraper.scrapeBooks import BookScraper
from quotescraper.scrapeQuotes import QuoteScraper
from base.base import Base
from exit.exit import UserExit, ProgramExit
from constants.constants import AGENT, BASE_URL
import os

# Important for a vnc server
# os.environ["DISPLAY"] = ":1"


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

            else:
                # Scrape Quotes
                scraper = QuoteScraper(BASE_URL + "/quotes", AGENT)

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
