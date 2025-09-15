from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
from exit.exit import UserExit, ProgramExit
from bs4 import BeautifulSoup


class Base:

    def __init__(self, url, user_agent):
        """Initializes the scraper, sets up the browser, and launches the starting page."""
        # Configure Chrome browser options
        options = Options()
        options.add_argument("--verbose")

        # Can be disabled for display
        options.add_argument("--headless=new")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--single-process")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        options.add_argument("--mute-audio")

        # Disable image for boosting (Can be removed for display)
        prefs = {"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option("prefs", prefs)

        options.add_argument(f"--user-agent={user_agent}")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def soup(self, source):
        """Creates a BeautifulSoup object from HTML source for easier parsing."""
        return BeautifulSoup(source, "html.parser")

    def close_popup(self):
        """Attempts to detect and close any modal popup by refreshing the page."""
        self.driver.implicitly_wait(10)
        current_url = self.driver.current_url

        try:
            # Check for a common modal popup
            modal_popup = self.soup(self.driver.page_source).find(
                "div", class_="modal__content")
            if modal_popup:
                self.driver.get(current_url)  # Refresh to dismiss popup

        except Exception as e:
            print(f"Error checking for popup: {e}")

    def get_user_choice(self):
        while True:
            print()
            print("=" * 50)
            print("What do you want to scrape?")
            print("*** 1: Get Books")
            print("*** 2: Get Quotes")
            print("*** 3: Start reading files")
            print("*** 4: Start clearing files")
            print("*** 5: Exit")
            user_in = input("\nPlease choose an option (1-5): ").strip()
            try:
                user_in = int(user_in)
                if user_in == 1:
                    return 1

                elif user_in == 2:
                    return 2

                elif user_in == 3:
                    return 3

                elif user_in == 4:
                    return 4

                elif user_in == 5:
                    raise UserExit("User requested exit.")

                else:
                    print(f"\n{'Enter a number between 1-5':_^10}")

            except ValueError:
                print(f"\n{'Please Enter A Number !':*>20}")

    def launch_page(self):
        """Navigates to the initial Goodreads URL and initiates the search flow."""
        self.driver.get(self.url)
