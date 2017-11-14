from providers.provider import *


class Idealista(Provider):
    def __init__(self):
        super().__init__()
        self.idealista_config = self.config["idealista"]

    def get_rooms(self):
        base_url = "https://secure.idealista.com/api/3.5/es/search?"
        params = "numPage={}&t=14960911059280.6039257777645473&k=5b85c03c16bbb85d96e232b112ee85dc".format(
            self.idealista_config['numPage'])
        headers = {
            "Authorization": "Bearer " + self.get_token(),
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        data = (
            ('timestamp', 1496533451607),
            ('token', 'de68ca7c68d4e72c7c2e0bb145cf1255'),
            ('user', 'ccwzckkcg@user.idealista.com'),
            ('order', self.idealista_config['order']),
            ('propertyType', self.idealista_config['propertyType']),
            ('smokingPolicy', self.idealista_config['smokingPolicy']),
            ('locale', self.idealista_config['locale']),
            ('maxItems', self.idealista_config['maxItems']),
            ('locationName', self.idealista_config['locationName']),
            ('petsPolicy', self.idealista_config['petsPolicy']),
            ('numPage', self.idealista_config['numPage']),
            ('hasMultimedia', self.idealista_config['hasMultimedia']),
            ('operation', self.idealista_config['operation']),
            ('locationId', self.idealista_config['locationId']),
            ('newGender', self.idealista_config['newGender']),
            ('minPrice', self.filters_config['minimum_price']),
            ('distance', self.idealista_config['distance']),
            ('sort', self.idealista_config['sort']),
            ('maxPrice', self.filters_config['maximum_price']),
            ('height', self.idealista_config['height']),
            ('width', self.idealista_config['width']),
            ('gallery', self.idealista_config['gallery']),
            ('quality', self.idealista_config['quality']),
        )
        url = base_url + params
        r = requests.post(url, data=data, headers=headers)
        return json.loads(r.content.decode('utf-8'))['elementList']

    def get_token(self):
        url = 'https://secure.idealista.com/api/oauth/token'
        headers = {
            "Authorization": "Basic NWI4NWMwM2MxNmJiYjg1ZDk2ZTIzMmIxMTJlZTg1ZGM6aWRlYSUzQmFuZHIwMWQ=",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        data = "grant_type=client_credentials&scope=write"
        r = requests.post(url, data=data, headers=headers)
        return json.loads(r.content.decode('utf-8'))['access_token']

    def get_room_description(self, room_id):
        url = 'https://secure.idealista.com/api/3/es/detail/' + str(room_id) + '?timestamp=1496600603025&token=2e234387068ddcf789c2d2cb5b9e6367&user=ccwzckkcg%40user.idealista.com&language=es&t=14960911059280.6039257777645473&k=5b85c03c16bbb85d96e232b112ee85dc'
        r = requests.get(url)
        json_description = json.loads(r.content.decode('utf-8'))
        if 'propertyComment' in json_description:
            return json_description['propertyComment']
        else:
            return None

    def populate_flat(self, room):
        flat = {
            "id": room['propertyCode'],
            "title": room['address'] + " - " + room['district'],
            "description": self.get_room_description(room['propertyCode']),
            "latitude": room['latitude'],
            "longitude": room['longitude'],
            "price": room['price'],
            "url": room['url'],
            "photos": room['numPhotos'],
            "rooms": room['rooms'],
            "bathrooms": room['bathrooms']
        }
        return flat

if __name__ == "__main__":
    Idealista = Idealista()
    rooms = Idealista.get_rooms()
    print(rooms)