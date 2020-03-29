import requests
import json
from sms import send_text_message
from weather_snapshot import get_weather_data


with open('variables.json') as f:
    variables = json.load(f)

coordinates = requests.get("https://ipinfo.io/loc").text.replace('\n', '').split(",")
city = requests.get("https://ipinfo.io/city").text.replace('\n', '')
state = requests.get("https://ipinfo.io/region").text.replace('\n', '')
weather_data = get_weather_data(key=variables['dark_sky_key'],
                                latitude=coordinates[0],
                                longitude=coordinates[1])

weather_text = '\n{}\n{}\n{}, {}\n\nTemperature: {}\nHigh: {}\nLow: {}\n\n{}\n{}'\
    .format(weather_data['current_time'],
            weather_data['current_date'],
            city,
            state,
            weather_data['current_temp'],
            weather_data['temp_high'],
            weather_data['temp_low'],
            weather_data['hourly_summary'],
            weather_data['daily_summary'])\
    .encode('utf-8')

send_text_message(to_number=variables['phone_number'],
                  to_carrier=variables['carrier'],
                  from_email=variables['email_address'],
                  from_password=variables['email_password'],
                  message=weather_text)
