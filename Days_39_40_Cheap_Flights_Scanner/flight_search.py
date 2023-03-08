import requests
from settings_manager import SettingsManager


class KiwiFlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, settings_manager: SettingsManager):
        self.kiwi_apikey = settings_manager.kiwi_apikey
        self.kiwi_api = 'https://api.tequila.kiwi.com'
        self.header = {
            'apikey': self.kiwi_apikey,
        }

    def get_iata_code(self, city):
        kiwi_endpoint = 'locations/query'
        parameters = {
            'term': city,
        }
        iata_response = requests.get(url=f'{self.kiwi_api}/{kiwi_endpoint}', params=parameters, headers=self.header)
        iata_response.raise_for_status()
        iata_code = iata_response.json()['locations'][0]['code']
        return iata_code

    def search_flight(self, city_from, city_to, date_from, date_to, maximal_price):
        kiwi_search_api = 'https://api.tequila.kiwi.com/v2/search'
        parameters = {
            'fly_from': city_from,
            'fly_to': city_to,
            'dateFrom': date_from,
            'dateTo': date_to,
            'max_stopovers': 2,
            'stopover_from': '2:30',
            'stopover_to': '12:00',
            'nights_in_dst_from': 1,
            'nights_in_dst_to': 13,
            'flight_type': 'round',
            'curr': 'EUR',
            'price_to': maximal_price,
        }
        search_response = requests.get(url=kiwi_search_api, params=parameters, headers=self.header)
        search_response.raise_for_status()
        return search_response.json()['data']

