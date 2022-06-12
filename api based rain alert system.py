import requests
from twilio.rest import Client


api_key = "Your API KEY"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "YOUR ACCOUNT SID" #Taken from twilio console portal.
auth_token = "Your auth_token number" #https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1&newCustomer=true

# For testing this api system one must have to take a lat. and long. of such place were rain fall is on going. To check that just visit
# https://www.ventusky.com/ and select precipitation.

weather_params = {
    "lat": 24.376930,  # Add your location co-ordinates i.e Latitude and longitude
    "lon": 88.603073,
    "appid": api_key,
    "exclude": "current,minutely,daily",

}


response = requests.get(OWM_ENDPOINT, params=weather_params)

# print(response.status_code) ## Check whether we get that response is running or not for this instant.
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])

weather_slice = weather_data["hourly"][:12]
# print(weather_slice)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        # print("Bring an umbrella")

if will_rain:
    # print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Hey Chaitanya! It's going to rain today. Remember to bring an ☔☂️☔☂️",
        from_='Enter your virtual number which you will getting from twilio',
        to='Your verified number at twilio account'
    )

    print(message.status)

## Upto this we can able get the one hour data but we want upto 12 hrs next data for that we will going to used python slice method. https://stackoverflow.com/questions/509211/understanding-slicing



