import requests
from settings_manager import SettingsManager
from pprint import pprint


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, settings_manager: SettingsManager):
        self.sheety_token = settings_manager.sheety_token
        self.sheety_endpoint = f'https://api.sheety.co/{self.sheety_token}/flightDeals'

    def get_all_flight_info(self):
        all_flight_response = requests.get(url=f'{self.sheety_endpoint}/prices')
        all_flight_response.raise_for_status()
        return all_flight_response.json()['prices']

    def get_users_info(self):
        all_flight_response = requests.get(url=f'{self.sheety_endpoint}/users')
        all_flight_response.raise_for_status()
        return all_flight_response.json()['users']

    def change_iata(self, id, iata):
        parameters = {
            'price': {
                'iataCode': iata,
            }
        }
        sheety_response = requests.put(url=f'{self.sheety_endpoint}/{id}', json=parameters)
        sheety_response.raise_for_status()
        pprint(sheety_response.json())




