from logo_scraper import scrape_logos
from product_scraper import scrape_products

brands = {
    "Khaadi": "https://www.khaadi.com/",
    "Gul Ahmed": "https://www.gulahmedshop.com/",
    "Sana Safinaz": "https://www.sanasafinaz.com/",
    "Alkaram Studio": "https://www.alkaramstudio.com/"
}

# scrape logos
logo_data = scrape_logos(brands)

print("\n\nFINAL LOGO DATA:")
print(logo_data)

# scrape products
product_data = scrape_products(brands)

print("\n\nFINAL PRODUCT DATA:")
print(product_data)