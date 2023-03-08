from data_manager import DataManager
from flight_search import KiwiFlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from settings_manager import SettingsManager
import datetime as dt


def main():
    settings_manager = SettingsManager()
    data_manager = DataManager(settings_manager)
    kiwi_flight_search = KiwiFlightSearch(settings_manager)
    notification_manager = NotificationManager(settings_manager)
    user_data = data_manager.get_users_info()
    sheet_data = data_manager.get_all_flight_info()
    today_date = dt.date.today()
    half_year_date = today_date + dt.timedelta(180)
    today_date_str = today_date.strftime('%d/%m/%Y')
    half_year_str = half_year_date.strftime('%d/%m/%Y')

    for route in sheet_data:
        if route['iataCode'] == '':
            route['iataCode'] = kiwi_flight_search.get_iata_code(route['city'])
            data_manager.change_iata(route['id'], route['iataCode'])

    for user in user_data:
        for route in sheet_data:
            flight_list = kiwi_flight_search.search_flight(
                user['homeIata'],
                route['iataCode'],
                today_date_str,
                half_year_str,
                route[user['homeIata'].lower()]
            )
            for flight in flight_list:
                flight_obj = FlightData(flight)
                print(notification_manager.send_notification(user['tgUserId'], flight_obj))


main()

