import requests

url = "https://flashlive-sports.p.rapidapi.com/v1/events/live-list"

querystring = {"timezone": "-4", "sport_id": "4", "locale": "en_INT"}

headers = {
	"X-RapidAPI-Key": "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
	"X-RapidAPI-Host": "flashlive-sports.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
