import rethinkdb as r
from configuration import Configuration
from data_store import DataStore


class ArticleDataStore:
    def __init__(self):
        config = Configuration()
        self.data_store = DataStore()
        self.db_host = config.get_db_host()
        self.db_port = config.get_db_port()
        self.db_username = config.get_db_username()
        self.db_password = config.get_db_password()
        self.db_name = config.get_db_name()
        self.db_article_table = config.get_article_table()

    def insert(self, title, category, description, date, site_url, url, image_url):
        try:
            conn = self.data_store.get_connection()
            entry_existing = r.table(self.db_article_table) \
                                 .get_all(title, index="title") \
                                 .count() \
                                 .run(conn) > 0

            if entry_existing:
                return

            r.table(self.db_article_table).insert({
                'title': title,
                'category': category,
                'description': description,
                'date': date,
                'site_url': site_url,
                'url': url,
                'image_url': image_url,
                'synchronised_to_discord': False
            }).run(conn)
        finally:
            DataStore.disconnect(conn)

    def get_unsynchronised(self):
        try:
            conn = self.data_store.get_connection()
            return r.table(self.db_article_table) \
                .filter({'synchronised_to_discord': False}) \
                .run(conn)
        finally:
            DataStore.disconnect(conn)

    def set_synchronised(self, unsynchronised_items):
        try:
            conn = self.data_store.get_connection()
            for item in unsynchronised_items:
                r.table(self.db_article_table) \
                    .get(item['id']) \
                    .update({"synchronised_to_discord": True}) \
                    .run(conn)
        finally:
            DataStore.disconnect(conn)

    def clear(self):
        try:
            conn = self.data_store.get_connection()
            r.table(self.db_article_table).delete().run(conn)
        finally:
            DataStore.disconnect(conn)
