 def created():
        conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")
        headers = {
            'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
            'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
        }
        conn.request(
            "GET", "/v1/events/live-list?timezone=-4&sport_id=1&locale=en_INT", headers=headers)
        res = conn.getresponse()
        data = res.read()
        parsed_data = json.loads(data.decode("utf-8"))

        try:
            with open("data.txt", "x") as file:
                file.write(str(parsed_data))
        except FileExistsError:
            with open("data.txt", "w") as file:
                file.write(str(parsed_data))

        pattern = r'"EVENT_ID":"([^"]+)"'
        matches = re.findall(pattern, str(parsed_data))
        print(matches)

        return Response(parsed_data)