class Output:
     def create_message(self, flat):
        message = ""
        if 'title' in flat:
            message += ">*Title:* {}\n".format(flat['title'])
        if 'description' in flat and flat['description'] != "" and flat["description"] is not None:
            message += ">*Description:* " + flat['description'].replace("\n", ". ") + "\n"
        if 'price' in flat:
            message += ">*Price:* " + str(flat['price']) + "€\n"
        if 'latitude' in flat and 'longitude' in flat:
            message += ">*Google Maps:* https://www.google.es/maps/place/" + str(flat['latitude']) + "," + \
                       str(flat['longitude']) + "\n"
        if 'url' in flat:
            message += "*URL:* " + flat['url']
        return message
