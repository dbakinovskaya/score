import requests

from .models import Events, Tournament, HockeyLiveEvents,TournamentHockey
from .serialaizers import EventsSerializer, HockeyLiveEventsSerializer
from django.db import transaction
from celery import shared_task


@shared_task
def send_request():
    with transaction.atomic():
        tournaments = Tournament.objects.all()
        events = Events.objects.all()

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
        for item in parsed_data['DATA']:
            tournament, _ = Tournament.objects.get_or_create(name=item['NAME'])
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
                    event_object, _ = Events.objects.get_or_create(event_id=event['EVENT_ID'])
                    serializer.update(event_object, serializer.validated_data)
                    tournament.events.add(event_object)
                else:
                    print(serializer.errors)

        # Удаление объектов модели Tournament и связанных объектов модели Events, которых нет в полученных данных
        tournaments.exclude(name__in=[item['NAME'] for item in parsed_data['DATA']]).delete()
        events.exclude(event_id__in=[event['EVENT_ID'] for item in parsed_data['DATA'] for event in item['EVENTS']]).delete()



@shared_task
def send_request_hockey():
    with transaction.atomic():
            tournament_hockey = TournamentHockey.objects.all()
            hockey_events = HockeyLiveEvents.objects.all()
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
                tournament_hockey, _ = TournamentHockey.objects.get_or_create(name=item['NAME'])
                tournament_hockey.tournament_stage_type = item['TOURNAMENT_STAGE_TYPE']
                tournament_hockey.tournament_imng = item['TOURNAMENT_IMAGE']
                tournament_hockey.TOURNAMENT_TEMPLATE_ID = item['TOURNAMENT_TEMPLATE_ID']
                tournament_hockey.save()
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
                        event_object, _ = HockeyLiveEvents.objects.get_or_create(event_id=event['EVENT_ID'])
                        serializer.update(event_object, serializer.validated_data)
                        tournament_hockey.hockey_events.add(event_object)
             # Удаление объектов модели Tournament и связанных объектов модели Events, которых нет в полученных данных
            tournament_hockey.exclude(name__in=[item['NAME'] for item in parsed_data['DATA']]).delete()
            hockey_events.exclude(EVENT_ID__in=[event['EVENT_ID'] for item in parsed_data['DATA'] for event in item['EVENTS']]).delete()                