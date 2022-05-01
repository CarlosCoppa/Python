import requests
from twilio.rest import Client
#API Key para realizar las llamadas
api_key = "2ee21c6be3de467692bed78dbd29fb97"

account_sid = "ACbf6bbbf00231b19ef98938bf327fdf13"
auth_token = "5f2d7f8188d9688ba0e0c1aeff69bed0"
#Endpoint del API
request = "https://api.openweathermap.org/data/2.5/onecall?"
#Params para configurar la llamada al API
params = {
    "lat": -26.159491,
    "lon": -58.189919,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

#Obtener el reporte del clima hora por hora
response = requests.get(url=request, params=params)
response.raise_for_status()
print(response)
data = response.json()
#print(data)

#Obtener el reporte solamente de las primeras doce horas
will_rain = False
hourly = data["hourly"][:12]
hourly_list = []
for hour in hourly:
    hourly_list.append(hour["weather"][0]["id"])
    if int(hour["weather"][0]["id"]) < 802:
        will_rain = True

print(hourly_list)
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an unbrella.",
                     from_='+19803242226',
                     to='+5493704801375'
                 )
    print(message.status)
    