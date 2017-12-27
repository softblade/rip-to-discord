# Article Scraper and Discord Sync

Simple python script to rip information from posts on sites and synchronise to Discord. Specifically put together to grab "Heroes of the Storm" news and "Guild Wars 2" news and sync it to Discord so that me and my friends can get notifications of updates to the games we enjoy in a single place (and the place we all communicate).

Mainly used as an exercise to learn [Python](https://www.python.org/), [RethinkDB](https://www.rethinkdb.com/) and to play with the [Discord API](https://discordapp.com/developers) so a bit rough (no proper error checking nor tests), but should be functional enough for simple use.

## Use

- Add a new .py script to the scraping/scrapers folder
- Add an entry in the config.json with the exact same name as the plugin file and the [webhook in Discord](https://support.discordapp.com/hc/en-us/articles/228383668-Intro-to-Webhooks).  For example, if you create a scraper, say "my_game.py", add the following entry to the configuration:

    ``` json
    {
        ...db settings here...
        "scrapers": [
            ...other scrapers...
            {
                "name": "my_game",
                "discord_channel": "hook url here"
            }
        ]
    }
    ```
- Executing "main.py -h" will show available commands:

    ``` bash
    --init      # Generate the necessary db and tables (will skip if exists)
    --scrape    # Runs the scrapers as defined in the config
    --post      # Post un-synchronised articles to Discord
    --force     # Force commands - currently only forces DB rebuild
    ```

## My Setup

Currently I am running it as follows:

1. I have RethinkDb docker image running on my Ubuntu 16 server
1. I have a cron-job to scrape for new news on a daily basis and posting to Discord running the script with the --scrape and --post arguments