import http.client

conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "2aedc6011bmsh0a810d06d659eafp102d45jsnac59d60c653c",
    'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
}

conn.request("GET", "/fixtures/live", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))