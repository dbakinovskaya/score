from urllib.parse import quote
import http.client
import asyncio
import re
import json
from django.db import connection
from django.db import transaction
from asgiref.sync import sync_to_async
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import LiveOfEvents, Events, EventId, Tournament
from .serialaizers import LiveOfEventsSerializer, EventsSerializer, EventLiveIdSerializer,TournamentSerializer
from .permissions import IsAdminOrReadOnly
import http.client


class EventIdViewSet(viewsets.ModelViewSet):
    queryset = EventId.objects.all()
    serializer_class = EventLiveIdSerializer
    # permission_classes = AllowAny

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
        # print(type(parsed_data))

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
    # permission_classes = AllowAny

    def get(self, request, live_event_id):
        event = get_object_or_404(EventId, live_event_id=live_event_id)
        h2h_data = h2h(event.live_event_id)
        statistics_data = events_statistic(event.live_event_id)
        lineups = events_start_lineps(event.live_event_id)
        odd = odds(event.live_event_id)

        serialized_data = json.dumps(
            {'h2h_data': h2h_data, 'statistics_data': statistics_data, 'lineups': lineups, 'odds': odd})

        return Response(serialized_data)


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    async def send_request(self):
        with transaction.atomic():
            Tournament.objects.all().delete()
            Events.objects.all().delete()

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
            for item in parsed_data['DATA']:
                tournament = Tournament()
                tournament.name = item['NAME']
                tournament.tournament_stage_type = item['TOURNAMENT_STAGE_TYPE']
                tournament.tournament_imng = item['TOURNAMENT_IMAGE']
                tournament.TOURNAMENT_TEMPLATE_ID = item['TOURNAMENT_TEMPLATE_ID']
                tournament.save()

                for event in item['EVENTS']:
                    data = {
                        'event_id': event['EVENT_ID'],
                        'start_time': event['START_TIME'],
                        'start_utime': event['START_UTIME'],
                        'game_time': event['GAME_TIME'],
                        'short_name_away': event['SHORTNAME_AWAY'],
                        'away_name': event['AWAY_NAME'],
                        'away_score_current': event['AWAY_SCORE_CURRENT'],
                        'away_score_part_1': event['AWAY_SCORE_PART_1'],
                        'away_score_part_2': event.get('AWAY_SCORE_PART_2', ''),
                        'short_name_home': event['SHORTNAME_HOME'],
                        'home_name': event['HOME_NAME'],
                        'home_score_current': event['HOME_SCORE_CURRENT'],
                        'home_score_part_1': event['HOME_SCORE_PART_1'],
                        'home_score_part_2': event.get('HOME_SCORE_PART_2', ''),
                    }
                    serializer = EventsSerializer(data=data)
                    if serializer.is_valid():
                        event_object = serializer.create(serializer.validated_data)
                        tournament.events.add(event_object)
                    else:
                        print(serializer.errors)

    async def schedule_request(self):
        while True:
            await self.send_request()
            await asyncio.sleep(10)

    def start_scheduling(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.schedule_request())
    
    def list(self, request):
        self.start_scheduling()
        return super().list(request)
    

class TournamentEventsViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    @sync_to_async
    def send_request(self):
        with transaction.atomic():
            Tournament.objects.all().delete()
            Events.objects.all().delete()

            conn = http.client.HTTPSConnection(
                "flashlive-sports.p.rapidapi.com")
            headers = {
                'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
                'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
            }
            conn.request(
                "GET", "/v1/events/live-list?timezone=-4&sport_id=1&locale=en_INT", headers=headers)
            res = conn.getresponse()
            data = res.read()
            parsed_data = json.loads(data.decode("utf-8"))
            for item in parsed_data['DATA']:
                tournament = Tournament()
                tournament.name = item['NAME']
                tournament.tournament_stage_type = item['TOURNAMENT_STAGE_TYPE']
                tournament.tournament_imng = item['TOURNAMENT_IMAGE']
                tournament.TOURNAMENT_TEMPLATE_ID = item['TOURNAMENT_TEMPLATE_ID']

                for event in item['EVENTS']:
                    data = {
                        'event_id': event['EVENT_ID'],
                        'start_time': event['START_TIME'],
                        'start_utime': event['START_UTIME'],
                        'game_time': event['GAME_TIME'],
                        'short_name_away': event['SHORTNAME_AWAY'],
                        'away_name': event['AWAY_NAME'],
                        'away_score_current': event['AWAY_SCORE_CURRENT'],
                        'away_score_part_1': event['AWAY_SCORE_PART_1'],
                        'away_score_part_2': event.get('AWAY_SCORE_PART_2', ''),
                        'away_images': event.get('AWAY_IMAGES', ''),
                        'short_name_home': event['SHORTNAME_HOME'],
                        'home_name': event['HOME_NAME'],
                        'home_score_current': event['HOME_SCORE_CURRENT'],
                        'home_score_part_1': event['HOME_SCORE_PART_1'],
                        'home_score_part_2': event.get('HOME_SCORE_PART_2', ''),
                        'home_images': event.get('HOME_IMAGES', '')
                    }
                    serializer = EventsSerializer(data=data)
                    if serializer.is_valid():
                        event_object = serializer.create(
                            serializer.validated_data)
                        tournament.events.add(event_object)
                    else:
                        print(serializer.errors)

                tournament.save()

    async def schedule_request(self):
        while True:
            await self.send_request()
            await asyncio.sleep(5)

    def start_scheduling(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.schedule_request())

    def list(self, request):
        tournaments = Tournament.objects.all()
        serializer = self.serializer_class(tournaments, many=True)
        return Response(serializer.data)    
