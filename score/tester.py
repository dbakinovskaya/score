import http.client

conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
    'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
}

conn.request("GET", "/v1/events/statistics?event_id=WtO7zDn5&locale=en_INT", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))