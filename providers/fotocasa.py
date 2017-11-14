from providers.provider import *


class Fotocasa(Provider):
    def __init__(self):
        super().__init__()
        self.fotocasa_config = self.config["fotocasa"]

    def get_rooms(self):
        base_url = 'https://api.fotocasa.es/PropertySearch/Search?'
        params = (
            ('transactionTypeId', self.fotocasa_config['transactionTypeId']),
            ('propertyTypeId', self.fotocasa_config['propertyTypeId']),
            ('isNewConstruction', self.fotocasa_config['isNewConstruction']),
            ('combinedLocationIds', self.fotocasa_config['combinedLocationIds']),
            ('latitude', self.fotocasa_config['latitude']),
            ('longitude', self.fotocasa_config['longitude']),
            ('pageNumber', self.fotocasa_config['pageNumber']),
            ('sortType', self.fotocasa_config['sortType']),
            ('sortOrderDesc', self.fotocasa_config['sortOrderDesc']),
            ('minPrice', self.filters_config['minimum_price']),
            ('maxPrice', self.filters_config['maximum_price']),
            ('culture', self.fotocasa_config['culture']),
            ('platformId', self.fotocasa_config['platformId']),
            ('hrefLangCultures', self.fotocasa_config['hrefLangCultures']),
        )
        url = base_url + urllib.parse.urlencode(params)
        headers = {
            "Content-Type": "application/json; charset=UTF-8"
        }
        r = requests.get(url, headers=headers)
        return json.loads(r.content.decode('utf-8'))['realEstates']

    def populate_flat(self, room):
        flat = {
            "id": room['id'],
            "title": room['address']['ubication'] + " - " + room['address']['location']['level7'],
            "description": room['description'],
            "latitude": room['address']['coordinates']['latitude'],
            "longitude": room['address']['coordinates']['longitude'],
            "price": room['transactions'][0]['value'][0],
            "url": "http://www.fotocasa.es" + room["detail"]["es"]
        }
        return flat
