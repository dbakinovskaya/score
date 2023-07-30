import requests
from .models import Events


url = "https://flashlive-sports.p.rapidapi.com/v1/events/live-list"
querystring = {
    "timezone": "-4",
    "sport_id": "1",
    "locale": "en_INT"
}
headers = {
    'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
    'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

dict_list = data['data']
event_list = []

for event_dict in dict_list:
    event_id = event_dict['EVENT_ID']
    event = Events(event_id)
    
    for key, value in event_dict.items():
        setattr(event, key.lower(), value)
    
    event_list.append(event)
print(event_list)    