from providers.provider import *


class Badi(Provider):
    def __init__(self):
        super().__init__()
        self.badi_config = self.config["badi"]

    def get_rooms(self):
        url = 'https://api.badiapp.com/v1/search/rooms'
        headers = {
            "Authorization": "Bearer cb146bab8f3126b3ffef666c9056e5eb8b33bd6ed7c218eb701d0417051a7a0a",
            "Content-Type": "application/json; charset=UTF-8"
        }
        data = {"city": self.badi_config['city'],
                "sort_by": self.badi_config['sort_by'],
                "bed_types": [2, 3],
                "amenities": [2, 9, 14, 18],
                "max_price": self.filters_config['maximum_price'],
                "new_search_mode": True,
                "page": self.badi_config['page'],
                "offset": self.badi_config['offset']}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        return json.loads(r.content.decode('utf-8'))

    def populate_flat(self, room):
        flat = {
            "id": room['id'],
            "title": room['title'],
            "description": room['description'],
            "latitude": room['latitude'],
            "longitude": room['longitude'],
            "price": room['prices_attributes'][0]['price'],
            "url": "https://www.badiapp.com/room/" + str(room['id'])
        }
        return flat
