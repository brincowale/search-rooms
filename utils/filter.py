import re


class Filter:
    def check_requirements(self, filters, flat):
        if 'description' not in flat or flat['description'] is None:
            return False
        if 'neighborhoods_inside_boundaries' in filters and 'latitude' in flat and 'longitude' in flat:
            for neighborhood in filters['neighborhoods_inside_boundaries']:
                if not self._is_flat_inside_neighborhood(neighborhood, flat['latitude'], flat['longitude']):
                    return False
        if 'neighborhoods_outside_boundaries' in filters and 'latitude' in flat and 'longitude' in flat:
            for neighborhood in filters['neighborhoods_outside_boundaries']:
                if not self._is_flat_outside_neighborhood(neighborhood, flat['latitude'], flat['longitude']):
                    return False
        if 'rooms' in flat and 'minimum_rooms' in filters and 'maximum_rooms' in filters:
            if not self._has_flat_desired_number_of_rooms(flat['rooms'], filters['minimum_rooms'], filters['maximum_rooms']):
                return False
        if 'bathrooms' in flat and 'minimum_bathrooms' in filters:
            if not self._has_flat_desired_number_of_bathrooms(flat['bathrooms'], filters['minimum_bathrooms']):
                return False
        if 'photos' in flat and 'minimum_photos' in filters:
            if not self._has_flat_desired_number_of_photos(flat['photos'], filters['minimum_photos']):
                return False
        if 'black_list_words' in filters and 'title' in flat:
            if not self._is_text_valid(filters['black_list_words'], flat['title']):
                return False
        if 'black_list_words' in filters and 'description' in flat:
            if not self._is_text_valid(filters['black_list_words'], flat['description']):
                return False
        if 'price' in flat and 'minimum_price' in filters and 'maximum_price' in filters:
            if not self._is_valid_price(flat['price'], filters['minimum_price'], filters['maximum_price']):
                return False
        return True

    def _is_flat_inside_neighborhood(self, boundaries, flat_latitude, flat_longitude):
        if boundaries[0] < flat_latitude < boundaries[2] and boundaries[1] < flat_longitude < boundaries[3]:
            return True
        return False

    def _is_flat_outside_neighborhood(self, boundaries, flat_latitude, flat_longitude):
        if self._is_flat_inside_neighborhood(boundaries, flat_latitude, flat_longitude):
            return False
        return True

    def _has_flat_desired_number_of_rooms(self, rooms_in_flat, minimum_desired_rooms, maximum_desired_rooms):
        if minimum_desired_rooms <= rooms_in_flat <= maximum_desired_rooms:
            return True
        return False

    def _has_flat_desired_number_of_bathrooms(self, bathrooms_in_flat, minimum_bathrooms):
        if bathrooms_in_flat >= minimum_bathrooms:
            return True
        return False

    def _has_flat_desired_number_of_photos(self, photos_of_flat, minimum_photos):
        if photos_of_flat >= minimum_photos:
            return True
        return False

    def _is_valid_price(self, flat_price, minimum_desired_price, maximum_desired_price):
        if minimum_desired_price <= flat_price <= maximum_desired_price:
            return True
        return False

    def _is_text_valid(self, phrases_to_check, text):
        for phrase in phrases_to_check:
            if phrase.lower() in text.lower():
                return False
        return True
