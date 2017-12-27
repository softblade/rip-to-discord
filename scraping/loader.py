import imp
import os

PluginFolder = "./scraping/scrapers"


def get_scrapers(scrapers):
    plugins = []
    possible_plugins = os.listdir(PluginFolder)
    for i in possible_plugins:
        module = i.replace(".py", "")
        if module not in scrapers:
            continue
        info = imp.find_module(module, [PluginFolder])
        plugins.append({"name": module, "info": info})
    return plugins


def load_scraper(name):
    return imp.load_module(name["name"], *name["info"])
