import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://news.ycombinator.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = []

for item in soup.find_all("span", class_="titleline"):
    titles.append(item.text)

df = pd.DataFrame({
    "Headlines": titles
})

df.to_excel("news_headlines.xlsx", index=False)

print("News data saved successfully!")
