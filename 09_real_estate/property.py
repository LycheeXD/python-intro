class Property:
    def __init__(self,
                 street, city, zip, state, beds, baths, sq__ft,
                 type, sale_date, price, latitude, longitude):
        self.street = street
        self.city = city
        self.zip = zip
        self.state = state
        self.beds = beds
        self.baths = baths
        self.sq__ft = sq__ft
        self.type = type
        self.sale_date = sale_date
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod
    def create_property(input_property):
        return Property(
            input_property['street'],
            input_property['city'],
            input_property['zip'],
            input_property['state'],
            int(input_property['beds']),
            int(input_property['baths']),
            int(input_property['sq__ft']),
            input_property['type'],
            input_property['sale_date'],
            float(input_property['price']),
            float(input_property['latitude']),
            float(input_property['longitude'])
        )
