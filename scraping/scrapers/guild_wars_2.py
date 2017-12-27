from bs4 import BeautifulSoup
import requests
from scraping.scrape_result import ScrapeResult


BASE_URL = "http://us.battle.net"
SITE_URL = "https://www.guildwars2.com/en-gb/news/"
IMAGE_URL = "https://guildwars2.staticwars.com/wp-content/themes/guildwars2.com-live/img/gw2-logo.a9bed23d.jpg"


def parse(category):
    r = requests.get(SITE_URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find("ul", {"class": "blogroll"}).find_all("li", {"class": "blog-post"})
    results = []
    for article in articles:
        title = article.find("h3", {"class": "blog-title"}).a.get_text().strip()
        description = article.find('div', {'class': 'bd'}).div.p.get_text().strip()
        date = article.find('div', {'class': 'meta'}).p.get_text().strip().replace("by The Guild Wars 2 Team on ", "")
        link = article.h3.a.get('href')
        image_url = IMAGE_URL
        result = ScrapeResult(title, category, description, date, BASE_URL, link, image_url)
        results.append(result)
    return results
