import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("article", class_="product_pod")

print("📚 Product Prices:\n")

for product in products[:5]:
    name = product.h3.a["title"]
    price = product.find("p", class_="price_color").text

    print(name)
    print("Price:", price)
    print("-" * 30)