from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_products(brands: dict, limit=5):
    results = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for brand, url in brands.items():
            print(f"\nScraping products: {brand}")

            try:
                page.goto(url, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_timeout(3000)

                soup = BeautifulSoup(page.content(), "html.parser")

                products = soup.select("a[href*='/products/']")

                product_list = []

                for p_tag in products[:limit]:
                    title = p_tag.get_text(strip=True)
                    link = p_tag.get("href")

                    full_link = urljoin(url, link)

                    product_list.append({
                        "title": title,
                        "url": full_link
                    })

                    print(title, full_link)

                results[brand] = product_list

            except Exception as e:
                results[brand] = []
                print("Error:", e)

        browser.close()

    return results