from bs4 import BeautifulSoup
import requests
from scraping.scrape_result import ScrapeResult


BASE_URL = "http://us.battle.net"
SITE_URL = "http://us.battle.net/heroes/en/blog/"


def parse(category):
    r = requests.get(SITE_URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find("div", {"class": "container news-index-section"}).find_all("article")
    results = []
    for article in articles:
        title = article.find("h2", {"class": "news-list__item__title"}).a.get_text().strip()
        description = article.find('p', {'class': 'news-list__item__description'}).get_text().strip()
        date = article.find('span', {'class': 'publish-date'}).get('title')
        link = f"{BASE_URL}{article.h2.a.get('href')}"
        image_url = f"http:{article.find('a', {'class': 'news-list__item__thumbnail'}).img.get('src')}"
        result = ScrapeResult(title, category, description, date, BASE_URL, link, image_url)
        results.append(result)
    return results
