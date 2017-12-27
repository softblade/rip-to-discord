import rethinkdb as r
from data_store import DataStore
from configuration import Configuration


def bootstrap_db(from_scratch):
    config = Configuration()
    conn = DataStore().get_connection()

    if from_scratch and config.get_db_name() in list(r.db_list().run(conn)):
        print('Forcing - dropping existing db')
        r.db_drop(config.get_db_name()).run(conn)

    if config.get_db_name() not in list(r.db_list().run(conn)):
        r.db_create(config.get_db_name()).run(conn)
    else:
        print(f"{config.get_db_name()} db already exists")

    if config.get_article_table() not in list(r.db(config.get_db_name()).table_list().run(conn)):
        r.db(config.get_db_name()).table_create(config.get_article_table()).run(conn)
        r.db(config.get_db_name()).table(config.get_article_table()).index_create('title').run(conn)
    else:
        print(f"{config.get_article_table()} table already exists")

    DataStore.disconnect(conn)
