import json


class SettingsManager:

    def __init__(self):
        with open('api_data.json', 'r') as data:
            api_data = json.load(data)
            self.token = api_data['tg_token']
            self.kiwi_apikey = api_data['kiwi_apikey']
            self.sheety_token = api_data['sheety_token']
            
