import requests
import json
import urllib.parse
from utils.filter import Filter

class Provider:
    def __init__(self):
        with open('data/config.json') as config_file:
            self.config = json.load(config_file)
        self.filters_config = self.config["filters"]
        self.filter = Filter()
