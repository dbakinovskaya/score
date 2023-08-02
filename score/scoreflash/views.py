from urllib.parse import quote
import http.client
import sqlite3
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
import http.client


class EventIdViewSet(viewsets.ModelViewSet):
    queryset = EventId.objects.all()
    serializer_class = EventLiveIdSerializer

    def list(self, request):
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


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


class LiveOfEventsViewSet(viewsets.ModelViewSet):
    queryset = LiveOfEvents.objects.all()
    serializer_class = LiveOfEventsSerializer

    def list(self, request):
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

        for event in parsed_data['DATA']:
            events = event['EVENTS']
            for ev in events:
                event_id = ev.get('EVENT_ID')
                start_time = ev.get('START_TIME')
                start_utime = ev.get('START_UTIME')
                stage_type = ev.get('STAGE_TYPE')
                merge_stage_type = ev.get('MERGE_STAGE_TYPE')
                stage = ev.get('STAGE')
                sort = ev.get('SORT')
                rounds = ev.get('ROUND')
                visible_run_rate = ev.get('VISIBLE_RUN_RATE')
                live_mark = ev.get('LIVE_MARK')
                has_lineps = ev.get('HAS_LINEPS')
                stage_start_time = ev.get('STAGE_START_TIME')
                game_time = ev.get('GAME_TIME')
                playing_on_sets = ev.get('PLAYING_ON_SETS')
                recent_overs = ev.get('RECENT_OVERS')
                shortname_home = ev.get('SHORTNAME_HOME')
                home_participant_ids = ev.get('HOME_PARTICIPANT_IDS')
                home_participant_types = ev.get('HOME_PARTICIPANT_TYPES')
                home_name = ev.get('HOME_NAME')
                home_event_participant_id = ev.get('HOME_PARTICIPANT_NAME_ONE')
                home_goal_var = ev.get('HOME_GOAL_VAR')
                home_score_current = ev.get('HOME_SCORE_CURRENT')
                home_score_part_1 = ev.get('HOME_SCORE_PART_1')
                home_score_part_2 = ev.get('HOME_SCORE_PART_2', None)
                home_images = ev.get('HOME_IMAGES')
                imm = ev.get('IMM')
                imw = ev.get('IMW')
                imp = ev.get('IMP')
                ime = ev.get('IME')
                shortname_away = ev.get('SHORTNAME_AWAY')
                away_participant_ids = ev.get('AWAY_PARTICIPANT_IDS')
                away_participant_types = ev.get('AWAY_PARTICIPANT_TYPES')
                away_name = ev.get('AWAY_NAME')
                away_participant_name_one = ev.get('AWAY_PARTICIPANT_NAME_ONE')
                away_event_participant_id = ev.get('AWAY_EVENT_PARTICIPANT_ID')
                away_goal_var = ev.get('AWAY_GOAL_VAR')
                away_score_current = ev.get('AWAY_SCORE_CURRENT')
                away_score_full = ev.get('AWAY_SCORE_FULL')
                away_score_part_1 = ev.get('AWAY_SCORE_PART_1')
                away_score_part_2 = ev.get('AWAY_SCORE_PART_2', None)
                away_images = ev.get('AWAY_IMAGES')
                an = ev.get('AN')
                has_live_centre = ev.get('HAS_LIVE_CENTRE')
                bookmakers_with_live_in_offer = ev.get(
                    'BOOKMAKERS_WITH_LIVE_IN_OFFER', None)
                live_in_offer_bookmaker_id = ev.get(
                    'LIVE_IN_OFFER_BOOKMAKER_ID', None)
                live_in_offer_status = ev.get('LIVE_IN_OFFER_STATUS')
                score_chance_away = ev.get('SCORE_CHANCE_AWAY', None)
                tv_live_streaming = ev.get('TV_LIVE_STREAMING', None)
                home_participant_name_one = ev.get('HOME_PARTICIPANT_NAME_ONE')
                try:
                    obj = Events()
                    obj = Events(event_id=event_id, start_time=start_time,
                                 start_utime=start_utime, stage_type=stage_type,
                                 merge_stage_type=merge_stage_type, stage=stage, sort=sort,
                                 rounds=rounds, visible_run_rate=visible_run_rate, live_mark=live_mark,
                                 has_lineps=has_lineps, stage_start_time=stage_start_time, game_time=game_time,
                                 playing_on_sets=playing_on_sets, recent_overs=recent_overs, shortname_home=shortname_home,
                                 home_participant_ids=home_participant_ids, home_participant_types=home_participant_types,
                                 home_name=home_name, home_event_participant_id=home_event_participant_id,
                                 home_goal_var=home_goal_var, home_score_current=home_score_current,
                                 home_score_part_1=home_score_part_1, home_score_part_2=home_score_part_2,
                                 home_images=home_images, imm=imm, imw=imw, imp=imp, ime=ime, shortname_away=shortname_away,
                                 away_participant_ids=away_participant_ids, away_participant_types=away_participant_types,
                                 away_name=away_name, away_participant_name_one=away_participant_name_one,
                                 away_event_participant_id=away_event_participant_id, away_goal_var=away_goal_var,
                                 away_score_current=away_score_current, away_score_full=away_score_full,
                                 away_score_part_1=away_score_part_1, away_score_part_2=away_score_part_2,
                                 away_images=away_images, an=an, has_live_centre=has_live_centre,
                                 bookmakers_with_live_in_offer=bookmakers_with_live_in_offer,
                                 live_in_offer_bookmaker_id=live_in_offer_bookmaker_id, live_in_offer_status=live_in_offer_status,
                                 score_chance_away=score_chance_away, tv_live_streaming=tv_live_streaming,
                                 home_participant_name_one=home_participant_name_one)
                    obj.save()
                except Exception as e:
                    print("Ошибка при сохранении ", str(e))

            return Response(data)


def h2h(event_id):
    conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
        'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
    }

    # encoded_event_id = quote(event_id, safe='')
    conn.request(
        "GET", f"/v1/events/h2h?locale=en_INT&event_id=82yYGQB9", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


# def events_statistic(event_id):
#     conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

#     headers = {
#         'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
#         'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
#     }
#     encoded_event_id = quote(event_id.encode('utf-8'), safe='')
#     conn.request(
#         "GET", f"/v1/events/statistics?event_id={encoded_event_id}&locale=en_INT", headers=headers)

#     res = conn.getresponse()
#     data = res.read()

#     print(data.decode("utf-8"))


# def events_statistic(event_id):
#     conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

#     headers = {
#         'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
#         'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
#     }

#     encoded_event_id = quote(event_id.encode('utf-8'), safe='')
#     conn.request(
#         "GET", f"/v1/events/statistics?event_id={encoded_event_id}&locale=en_INT", headers=headers)

#     res = conn.getresponse()
#     data = res.read()

#     print(data.decode("utf-8"))


# def events_start_lineps(event_id):

#     conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

#     headers = {
#         'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
#         'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
#     }
#     encoded_event_id = quote(event_id.encode('utf-8'), safe='')
#     conn.request(
#         "GET", f"/v1/events/lineups?event_id={encoded_event_id}&locale=en_INT", headers=headers)

#     res = conn.getresponse()
#     data = res.read()

#     print(data.decode("utf-8"))


# def odds(event_id):
#     conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

#     headers = {
#         'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
#         'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
#     }

#     encoded_event_id = quote(event_id.encode('utf-8'), safe='')
#     conn.request(
#         "GET", f"/v1/events/odds?event_id={encoded_event_id}&locale=en_INT", headers=headers)

#     res = conn.getresponse()
#     data = res.read()

#     print(data.decode("utf-8"))


class EventDetails(APIView):
    def get(self, request, event_id):
        event_id = get_object_or_404(Events, event_id=event_id)

        # Вызываем функции, передавая значение event_id
        h2h_data = h2h(event_id)
        # events_statistic_data = events_statistic(event_id)
        # events_start_lineps_data = events_start_lineps(event_id)
        # odds_data = odds(event_id)

        # Выводим данные на экран
        # print('Event ID:', event_id)
        print('H2H Data:', h2h_data)
        # print('Events Statistic Data:', events_statistic_data)
        # print('Events Start Lineps Data:', events_start_lineps_data)
        # print('Odds Data:', odds_data)

        # Создаем JSON-ответ
        response = {
            # 'event_id': event_id,
            'h2h_data': h2h_data,
            # 'events_statistic_data': events_statistic_data,
            # 'events_start_lineps_data': events_start_lineps_data,
            # 'odds_data': odds_data
        }

        # Возвращаем JSON-ответ
        return Response(response)
