import requests
from bs4 import BeautifulSoup

url = "https://example.com/products"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_="product")

for product in products:
    name = product.find("h2").text
    price = product.find("span", class_="price").text

    print(name, price)