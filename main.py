from configuration import Configuration
from article_data_store import ArticleDataStore
from discord.sync_to_discord import SyncToDiscord
import scraping.loader as loader
import argparse
from bootstrap.bootstrap_db import bootstrap_db


parser = argparse.ArgumentParser()
parser.add_argument('--init', help='initialise the rethink database', dest='do_init', nargs='?', const=True, type=bool)
parser.add_argument('--scrape', help='run the scrapers and update the database', dest='do_scrape', nargs='?', const=True, type=bool)
parser.add_argument('--post', help='post newly scraped messages to Discord', dest='do_post', nargs='?', const=True, type=bool)
parser.add_argument('--force', help='force action', nargs='?', const=True, type=bool)
args = parser.parse_args()

if args.do_init:
    print('Initialising DB...')
    bootstrap_db(args.force)
    print('Done\n')

if args.do_scrape:
    print('Scraping...')
    conf = Configuration()
    scrapers = list(map(lambda a: a['name'], conf.get_scrapers()))
    results = []
    actual_scrapers = loader.get_scrapers(scrapers)
    for i in actual_scrapers:
        print("Loading scraper " + i["name"])
        scraper = loader.load_scraper(i)
        results = results + scraper.parse(i["name"])

    print('\nUpdating DB...')
    data_store = ArticleDataStore()
    for result in results:
        data_store.insert(
            result.get_title(),
            result.get_category(),
            result.get_description(),
            result.get_date(),
            result.get_site_url(),
            result.get_url(),
            result.get_image_url())
    print('Done\n')

if args.do_post:
    print('Posting to Discord...')
    news_items = list(data_store.get_unsynchronised())
    conf = Configuration()
    scrapers = conf.get_scrapers()
    for scraper in scrapers:
        sync_client = SyncToDiscord(conf.get_discord_channel(scraper))
        items = list(filter(lambda a: a['category'] == scraper['name'], news_items))
        sync_client.sync(items)
    data_store.set_synchronised(news_items)
    print('Done\n')

print('Done\n')
