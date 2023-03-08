class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, flight):
        self.price = flight['price']
        self.departure_airport_code = flight['flyFrom']
        self.arrival_airport_code = flight['flyTo']
        self.departure_city = flight['cityFrom']
        self.arrival_city = flight['cityTo']
        self.departure_date, self.departure_local_time = flight['route'][0]['local_departure'].split('T')
        self.departure_local_time = self.departure_local_time[:5]
        self.stopovers_num = len(flight['route'])-2
        self.nights_in_dest = flight['nightsInDest']
        self.via = []
        for item in flight['route']:
            if item['flyTo'] != self.arrival_airport_code and item['flyFrom'] != self.departure_airport_code:
                if item['flyFrom'] not in self.via:
                    self.via.append(item['flyFrom'])

