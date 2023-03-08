This project utilizes Google Sheets (Sheety.co) API, Kiwi API and Telegram API to provide updates on cheap flight prices for specific destinations. The aim of the project is to help users find the cheapest flights available for their desired destinations.

The project works by extracting user data, flight destinations, and minimum flight prices from a designated Google Sheets. It then queries the Kiwi API for real-time flight prices to the same destinations. If the current flight prices are lower than the minimum prices set by the user, the project sends a notification message to a designated Telegram bot.

The project is built using Python and leverages the Google Sheets API and Kiwi API to retrieve and process data. It also uses the Telegram API to send notification messages to the Telegram bot.

To use the project, users will need to provide their Google Sheets API key, Kiwi API key, and Telegram bot API key. The project can be customized to work with any Google Sheet containing relevant data and can be modified to retrieve data from other APIs if required.
