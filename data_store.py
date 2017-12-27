import rethinkdb as r
from configuration import Configuration


class DataStore:
    def __init__(self):
        config = Configuration()
        self.db_host = config.get_db_host()
        self.db_port = config.get_db_port()
        self.db_username = config.get_db_username()
        self.db_password = config.get_db_password()
        self.db_name = config.get_db_name()
        self.db_article_table = config.get_article_table()

    def get_connection(self):
        if self.db_username is None:
            return r.connect(
                host=self.db_host,
                port=self.db_port,
                db=self.db_name)
        else:
            return r.connect(
                host=self.db_host,
                port=self.db_port,
                user=self.db_username,
                password=self.db_password,
                db=self.db_name)

    @staticmethod
    def disconnect(connection):
        connection.close()
