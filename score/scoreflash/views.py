import http.client
import asyncio
import requests
import time
import schedule
import threading
import json

from django.db import transaction
from asgiref.sync import sync_to_async
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Events, EventId, Tournament, HockeyLiveEvents, TournamentHockey
from .serialaizers import (EventsSerializer, EventLiveIdSerializer,
                           TournamentSerializer, TournamentHockeySerializer, HockeyLiveEventsSerializer)

import http.client


class EventIdViewSet(viewsets.ModelViewSet):
    queryset = EventId.objects.all()
    serializer_class = EventLiveIdSerializer

    def list_ev(self, request):
        # Удаление данных из таблицы
        EventId.objects.all().delete()
        event_ids = Events.objects.values_list('event_id', flat=True)
        for event_id in event_ids:
            live_event = EventId(live_event_id=event_id)
            live_event.save()

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
    '''Вью для деталей матча '''
    # permission_classes = AllowAny

    def get(self, request, live_event_id):
        event = get_object_or_404(EventId, live_event_id=live_event_id)
        h2h_data = h2h(event.live_event_id)
        statistics_data = events_statistic(event.live_event_id)
        lineups = events_start_lineps(event.live_event_id)
        odd = odds(event.live_event_id)

        serialized_data = json.dumps(
            {'statistics_data': statistics_data})

        return Response(serialized_data)


class TournamentViewSet(viewsets.ModelViewSet):
    ''' Основаной вью для лайва'''
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    def start_scheduling(self):
        # Запускаем функцию send_request каждые 5 секунд
        schedule.every(5).seconds.do(self.send_request)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def send_request(self):
        with transaction.atomic():
            Tournament.objects.all().delete()
            Events.objects.all().delete()

            url = "https://flashlive-sports.p.rapidapi.com/v1/events/live-list"
            headers = {
                'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
                'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
            }
            params = {
                'timezone': '-4',
                'sport_id': '1',
                'locale': 'en_INT'
            }

            response = requests.get(url, headers=headers, params=params)
            parsed_data = response.json()
            print(parsed_data)
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
                        'home_images': event.get('HOME_IMAGES'),
                        'away_images': event.get('AWAY_IMAGES'),
                    }
                    serializer = EventsSerializer(data=data)
                    if serializer.is_valid():
                        event_object = serializer.create(
                            serializer.validated_data)
                        tournament.events.add(event_object)
                    else:
                        print(serializer.errors)

    def list(self, request):
        # Запускаем поток для выполнения start_scheduling
        thread = threading.Thread(target=self.start_scheduling)
        thread.start()
        tournaments = Tournament.objects.all()
        serializer = self.serializer_class(tournaments, many=True)
        event_viewset = EventIdViewSet()
        event_viewset.list_ev(request)
        return Response(serializer.data)




class HockeyView(viewsets.ModelViewSet):
    '''Основной вью для хоккея'''
    queryset = TournamentHockey.objects.all()
    serializer_class = TournamentHockeySerializer

    def start_scheduling(self):
        # Запускаем функцию send_request каждые 5 секунд
        schedule.every(5).seconds.do(self.send_request)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def send_request(self):
        with transaction.atomic():
            TournamentHockey.objects.all().delete()
            HockeyLiveEvents.objects.all().delete()
            url = "https://flashlive-sports.p.rapidapi.com/v1/events/live-list"
            headers = {
                'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
                'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
            }
            params = {
                'timezone': '-4',
                'sport_id': '4',
                'locale': 'en_INT'
            }

            response = requests.get(url, headers=headers, params=params)
            parsed_data = response.json()
            for item in parsed_data['DATA']:
                tournament = TournamentHockey()
                tournament.name = item['NAME']
                tournament.tournament_stage_type = item['TOURNAMENT_STAGE_TYPE']
                tournament.tournament_imng = item['TOURNAMENT_IMAGE']
                tournament.TOURNAMENT_TEMPLATE_ID = item['TOURNAMENT_TEMPLATE_ID']
                tournament.save()
                for event in item['EVENTS']:
                    data = {
                        'EVENT_ID': event['EVENT_ID'],
                        'START_TIME': event['START_TIME'],
                        'START_UTIME': event['START_UTIME'],
                        'GAME_TIME': event['GAME_TIME'],
                        'SHORTNAME_AWAY': event['SHORTNAME_AWAY'],
                        'AWAY_NAME': event['AWAY_NAME'],
                        'AWAY_SCORE_CURRENT': event['AWAY_SCORE_CURRENT'],
                        'AWAY_SCORE_PART_1': event['AWAY_SCORE_PART_1'],
                        'AWAY_SCORE_PART_2': event.get('AWAY_SCORE_PART_2', ''),
                        'AWAY_IMAGES': event.get('AWAY_IMAGES', ''),
                        'SHORTNAME_HOME': event['SHORTNAME_HOME'],
                        'HOME_NAME': event['HOME_NAME'],
                        'HOME_SCORE_CURRENT': event['HOME_SCORE_CURRENT'],
                        'HOME_SCORE_PART_1': event['HOME_SCORE_PART_1'],
                        'HOME_SCORE_PART_2': event.get('HOME_SCORE_PART_2', ''),
                        'HOME_IMAGES': event.get('HOME_IMAGES', ''),
                        'STAGE_TYPE': event['STAGE_TYPE'],
                        'MERGE_STAGE_TYPE': event['MERGE_STAGE_TYPE'],
                        'STAGE': event['STAGE'],
                        'SORT': event['SORT'],
                        'LIVE_MARK': event['LIVE_MARK'],
                        'HAS_LINEPS': event['HAS_LINEPS'],
                        'STAGE_START_TIME': event['STAGE_START_TIME'],
                        'PLAYING_ON_SETS': event['PLAYING_ON_SETS'],
                        'RECENT_OVERS': event['RECENT_OVERS'],
                        'HOME_PARTICIPANT_NAME_ONE': event['HOME_PARTICIPANT_NAME_ONE'],
                        'HOME_EVENT_PARTICIPANT_ID': event['HOME_EVENT_PARTICIPANT_ID'],
                        'HOME_GOAL_VAR': event['HOME_GOAL_VAR'],
                        'HOME_SCORE_PART_3': event.get('HOME_SCORE_PART_3', ''),
                        'AWAY_PARTICIPANT_NAME_ONE': event['AWAY_PARTICIPANT_NAME_ONE'],
                        'AWAY_EVENT_PARTICIPANT_ID': event['AWAY_EVENT_PARTICIPANT_ID'],
                        'AWAY_GOAL_VAR': event['AWAY_GOAL_VAR'],
                        'AWAY_SCORE_FULL': event['AWAY_SCORE_FULL'],
                        'AWAY_SCORE_PART_3': event.get('AWAY_SCORE_PART_3', '')
                    }
                    serializer = HockeyLiveEventsSerializer(data=data)
                    if serializer.is_valid():
                        event_object = serializer.create(
                            serializer.validated_data)
                        tournament.events_hockey.add(event_object)
                        # else:
                        #     print(serializer.errors)

    def list(self, request):
        # Запускаем поток для выполнения start_scheduling
        thread = threading.Thread(target=self.start_scheduling)
        thread.start()
        tournaments = TournamentHockey.objects.all()
        serializer = self.serializer_class(tournaments, many=True)
        # event_viewset = EventIdViewSet()
        # event_viewset.list_ev(request)
        return Response(serializer.data)
