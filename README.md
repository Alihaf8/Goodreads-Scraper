
# Goodreads Scraper

A powerful and efficient Python scraper built with Selenium and BeautifulSoup4 to extract detailed information about books and quotes from Goodreads.com. This tool features a user-friendly menu-driven interface and is designed to mimic human browsing behavior to avoid detection.

> **Note:** This project was developed entirely on a mobile device using Termux, demonstrating its capability to run in resource-constrained environments.

## ✨ Features

### Book Scraper
*   **Search:** Search for books by title.
*   **Pagination:** Navigate through multiple pages of search results.
*   **Detailed Extraction:** For any selected book, scrape:
    *   Title, Author(s), & Rating
    *   Genres & Description
    *   Publication info, Page count, & Language
    *   Main characters

### Quote Scraper
*   **Topic Search:** Search quotes by topic (e.g., Love, Wisdom, Life).
*   **Pagination:** Browse through pages of quote results.

### Core Features
*   **Stealthy:** Uses randomized delays and user-agent rotation to appear human.
*   **Robust:** Handles pop-ups and errors gracefully.
*   **Menu-Driven:** Easy-to-use text-based interface.
*   **Data Export:** Save scraped book data to a structured CSV file.

## 🛠️ Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Alihaf8/Goodreads-Scraper.git goodreads
    cd goodreads
    ```
> **Note:** Do not attempt to change the folder name ``` goodreads ``` ! or the project might get broken.
2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Install ChromeDriver:**
    This project requires `chromedriver` to be installed and available in your system PATH.
    *   **On Termux (Android):** You can install it with:
        ```bash
        pkg install chromium chromedriver
        ```
        or
        ```bash
         pkg install chromium -y
        ```
    *   **On Other Systems:** Download it from the [official site](https://sites.google.com/chromium.org/driver/) and ensure it's accessible.

## 🚀 Usage

1.  Navigate to the project directory.
2.  Run the main script:
    ```bash
    python runner.py
    ```
3.  Follow the interactive menus to:
    *   Choose between scraping **Books** or **Quotes**.
    *   Enter your search query.
    *   Navigate results and view details.

## 📁 Project Structure
