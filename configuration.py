import json


class Configuration:
    def __init__(self):
        self.config = None

    def get_configuration(self):
        if self.config is not None:
            return self.config
        with open('config.json', 'r') as f:
            self.config = json.load(f)
        return self.config

    def get_db_configuration(self):
        return self.get_configuration()['db']

    def get_db_name(self):
        return self.get_db_configuration()['name']

    def get_db_host(self):
        return self.get_db_configuration()['host']

    def get_db_port(self):
        return self.get_db_configuration()['port']

    def get_db_username(self):
        return self.get_db_configuration()['user']

    def get_db_password(self):
        return self.get_db_configuration()['password']

    def get_article_table(self):
        return self.get_db_configuration()['article_table']

    def get_scrapers(self):
        return self.get_configuration()['scrapers']

    def get_discord_channel(self, scraper):
        return scraper['discord_channel']