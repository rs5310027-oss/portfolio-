import requests
from bs4 import BeautifulSoup

url = "https://remoteok.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("td", class_="company")

for job in jobs:
    print(job.text.strip())