from urllib.parse import quote
import http.client
import asyncio
import re
import json
from django.db import connection

from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import LiveOfEvents, Events, EventId
from .serialaizers import LiveOfEventsSerializer, EventsSerializer, EventLiveIdSerializer
from .permissions import IsAdminOrReadOnly
import http.client


class EventIdViewSet(viewsets.ModelViewSet):
    queryset = EventId.objects.all()
    serializer_class = EventLiveIdSerializer
    permission_classes = IsAdminOrReadOnly

    def list(self, request):
        # Удаление данных из таблицы
        EventId.objects.all().delete()

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
        print(type(parsed_data))

        for item in parsed_data['DATA']:
            for event in item['EVENTS']:
                live_event = EventId(live_event_id=event['EVENT_ID'])
                live_event.save()

        return Response(parsed_data)

    async def send_request(self):
        self.list(None)

    async def schedule_request(self):
        while True:
            await self.send_request()  # Выполняем запрос
            await asyncio.sleep(0.33)  # Подождать 0.33 секунды

    def start_scheduling(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.schedule_request())
        loop.run_forever()


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


def h2h(live_event_id):
    conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
        'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
    }

    url = f"/v1/events/h2h?locale=en_INT&event_id={live_event_id}"
    url = url.replace(" ", "")
    print(url)
    conn.request("GET", url, headers=headers)

    res = conn.getresponse()
    data = res.read()

    return json.loads(data.decode("utf-8"))


def events_statistic(live_event_id):
    conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
        'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
    }
    # encoded_event_id = quote(event_id.encode('utf-8'), safe='')
    url = f"/v1/events/statistics?event_id={live_event_id}&locale=en_INT"
    url = url.replace(" ", "")
    conn.request(
        "GET", url, headers=headers)

    res = conn.getresponse()
    data = res.read()

    return json.loads(data.decode("utf-8"))


def events_start_lineps(live_event_id):

    conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
        'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
    }
    url = f"/v1/events/lineups?event_id={live_event_id}&locale=en_INT"
    url = url.replace(" ", "")
    conn.request(
        "GET", url, headers=headers)

    res = conn.getresponse()
    data = res.read()

    return json.loads(data.decode("utf-8"))


def odds(live_event_id):
    conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
        'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
    }

    url = f"/v1/events/odds?event_id={live_event_id}&locale=en_INT"
    url = url.replace(" ", "")
    conn.request(
        "GET", url, headers=headers)

    res = conn.getresponse()
    data = res.read()

    return json.loads(data.decode("utf-8"))


class EventDetails(APIView):
    permission_classes = IsAdminOrReadOnly
    
    def get(self, request, live_event_id):
        event = get_object_or_404(EventId, live_event_id=live_event_id)
        h2h_data = h2h(event.live_event_id)
        statistics_data = events_statistic(event.live_event_id)
        lineups = events_start_lineps(event.live_event_id)
        odd = odds(event.live_event_id)

        serialized_data = json.dumps(
            {'h2h_data': h2h_data, 'statistics_data': statistics_data, 'lineups': lineups, 'odds': odd})

        return Response(serialized_data)
