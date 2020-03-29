import requests
import json
import datetime


def get_weather_data(key, longitude, latitude):
    url = 'https://api.darksky.net/forecast/'
    exclude = 'minutely,alerts,flags'
    request = requests.get('{}{}/{},{}?exclude={}'.format(url, key, latitude, longitude, exclude))
    weather_data = json.loads(request.text)

    current_timestamp = weather_data['currently']['time']
    current_date_object = datetime.datetime.fromtimestamp(current_timestamp)

    current_time = current_date_object.strftime('%I:%M %p')
    current_date = current_date_object.strftime('%A, %B %d, %Y')
    current_temp = weather_data['currently']['temperature']
    temp_high = weather_data['daily']['data'][0]['temperatureHigh']
    temp_low = weather_data['daily']['data'][0]['temperatureLow']
    hourly_summary = weather_data['hourly']['summary']
    daily_summary = weather_data['daily']['summary']

    return {
        'current_time': current_time,
        'current_date': current_date,
        'current_temp': current_temp,
        'temp_high': temp_high,
        'temp_low': temp_low,
        'hourly_summary': hourly_summary,
        'daily_summary': daily_summary
    }
