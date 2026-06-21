from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_logos(brands: dict):
    results = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for brand, url in brands.items():
            print(f"\nScraping logo: {brand}")

            try:
                page.goto(url, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(3000)

                soup = BeautifulSoup(page.content(), "html.parser")

                logo = (
                    soup.select_one("img[class*='logo']") or
                    soup.select_one("img[alt*='logo']") or
                    soup.select_one("header img") or
                    soup.find("img")
                )

                if logo:
                    logo_url = urljoin(url, logo.get("src"))
                    results[brand] = logo_url
                    print("Logo:", logo_url)
                else:
                    results[brand] = None
                    print("Logo not found")

            except Exception as e:
                results[brand] = None
                print("Error:", e)

        browser.close()

    return results