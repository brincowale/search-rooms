# README #

### What is this repository for? ###

Find rooms in shared flats in the websites: Idealista, Fotocasa, Idealista and receive the flats in a Slack channel.
It's not difficult to add other providers and also it's compatible with entire flats with some tweeks.
There's a config.json file that allows filter your searches by number of rooms, avoid some areas and include others,
minimum number of pictures, exclude words...


### How do I get set up? ###

* Python 3
* Install Python packages: slackclient, requests
* Modify config.json
* Run (and edit if needed) the main script run.py

### What else ? ###

This program can be adapted easily to other requirements.
* The current storage is sqlite and all the queries are managed from database.py. Example: replace sqlite by postgres editing this file only
* The output is managed from slack.py that extends from output.py. Example: replace slack by a custom telegram.py
* Changes the search parameters from any provider from config.json. Example: replace the beedroom search by a entire flat