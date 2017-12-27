from scraping.scrape_result import ScrapeResult


def parse(category):
    results = []
    for article in range(0, 2):
        result = ScrapeResult(article, category, article, article, article, article, article)
        results.append(result)
    return results
