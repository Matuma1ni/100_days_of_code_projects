import requests
from settings_manager import SettingsManager
from flight_data import FlightData
import datetime as dt


class NotificationManager:
    def __init__(self, settings_manager: SettingsManager):
        self.token = settings_manager.token
        self.message_api = f'https://api.telegram.org/bot{self.token}/sendMessage'

    def check_messages(self):
        tg_response = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
        print(tg_response.json())

    def send_notification(self, tg_user_id, flight: FlightData):
        chatID = tg_user_id
        stopover_message = ''
        return_date = dt.date.fromisoformat(flight.departure_date) + dt.timedelta(flight.nights_in_dest)
        kiwi_link = f'https://www.kiwi.com/en/search/results/{flight.departure_airport_code}/' \
                    f'{flight.arrival_airport_code}/{flight.departure_date}/{return_date}' \
                    f'/?stopDurationMax=12&stopNumber=1~true'
        if flight.stopovers_num > 0:
            if len(flight.via) > 1:
                via_message = ', '.join(flight.via)
            else: via_message = flight.via[0]
            stopover_message = f' via {via_message} with {flight.stopovers_num} stopover(s) total'
        bot_message = f'✈ Low price alert! Only {flight.price}€ to fly ' \
                      f'from {flight.departure_city}-{flight.departure_airport_code} ' \
                      f'on {flight.departure_date} at {flight.departure_local_time} ' \
                      f'to {flight.arrival_city}-{flight.arrival_airport_code} ' \
                      f'with {flight.nights_in_dest} nights in destination city'\
                      f'{stopover_message}\n{kiwi_link}'
        parameters = {
            'chat_id': chatID,
            'parse_mode': 'Markdown',
            'text': bot_message
        }
        response = requests.get(self.message_api, params=parameters)
        return response.json()