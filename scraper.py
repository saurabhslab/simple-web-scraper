import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Hacker News uses the class 'titleline' for headlines
headlines = soup.select(".titleline")

for i, headline in enumerate(headlines[:5], start=1):
    title = headline.text.strip()
    print(f"{i}. {title}")


