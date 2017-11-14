from providers.badi import Badi
from providers.fotocasa import Fotocasa
from providers.idealista import Idealista
from output.slack import Slack
from data.database import Database

badi = Badi()
idealista = Idealista()
fotocasa = Fotocasa()
slack = Slack(badi.config['slack'])
db = Database(badi.config["database"])


rooms = badi.get_rooms()
for room in rooms:
    flat = badi.populate_flat(room)
    if badi.filter.check_requirements(badi.filters_config, flat):
        db.insert(flat, "badi")

rooms = idealista.get_rooms()
for room in rooms:
    flat = idealista.populate_flat(room)
    if idealista.filter.check_requirements(idealista.filters_config, flat):
        db.insert(flat, "idealista")

rooms = fotocasa.get_rooms()
for room in rooms:
    flat = fotocasa.populate_flat(room)
    if fotocasa.filter.check_requirements(fotocasa.filters_config, flat):
        db.insert(flat, "fotocasa")


providers = ['badi', 'idealista', 'fotocasa']
for provider in providers:
    for flat in db.select_news(provider):
        message = slack.create_message(flat)
        slack.send_message(message)
        db.update_readed(flat['id'], provider)


db.close()