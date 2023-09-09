import requests
import time

from django.utils import timezone

from .models import Events, Tournament, HockeyLiveEvents, TournamentHockey, EndedMatch, Scheduled
from .serialaizers import EventsSerializer, HockeyLiveEventsSerializer
from django.db import transaction
from celery import shared_task


@shared_task
def send_request():
    try:
        with transaction.atomic():
            Tournament.objects.all().select_for_update().delete()
            Events.objects.all().select_for_update().delete()
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
            try:
                for item in parsed_data['DATA']:
                    tournaments = Tournament.objects.filter(name=item['NAME'])
                    if tournaments.exists():
                        tournament = tournaments.first()
                    else:
                        tournament = Tournament.objects.create(
                            name=item['NAME'],
                            tournament_stage_type=item['TOURNAMENT_STAGE_TYPE'],
                            tournament_imng=item['TOURNAMENT_IMAGE'],
                            TOURNAMENT_TEMPLATE_ID=item['TOURNAMENT_TEMPLATE_ID']
                        )
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
                            event_objects = Events.objects.filter(
                                event_id=event['EVENT_ID'])
                            if event_objects.exists():
                                event_object = event_objects.first()
                                serializer.update(
                                    event_object, serializer.validated_data)
                            else:
                                event_object = Events.objects.create(
                                    **serializer.validated_data)
                            tournament.events.add(event_object)
                        else:
                            print(serializer.errors)
            except KeyError:
                pass
    except Exception:
        pass


@shared_task
def send_request_hockey():
    try:
        with transaction.atomic():
            # tournament_hockey = TournamentHockey.objects.all()
            # hockey_events = HockeyLiveEvents.objects.all()
            TournamentHockey.objects.all().select_for_update().delete()
            HockeyLiveEvents.objects.all().select_for_update().delete()

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
            try:
                for item in parsed_data['DATA']:
                    tournament = TournamentHockey.objects.filter(
                        name=item['NAME'])
                    if tournament.exists():
                        tournament = tournament.first()
                    else:
                        tournament = TournamentHockey.objects.create(
                            name=item['NAME'],
                            tournament_stage_type=item['TOURNAMENT_STAGE_TYPE'],
                            tournament_imng=item['TOURNAMENT_IMAGE'],
                            TOURNAMENT_TEMPLATE_ID=item['TOURNAMENT_TEMPLATE_ID']
                        )
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
                            event_objects = HockeyLiveEvents.objects.filter(
                                EVENT_ID=event['EVENT_ID'])
                            if event_objects.exists():
                                event_object = event_objects.first()
                                serializer.update(
                                    event_object, serializer.validated_data)
                            else:
                                event_object = HockeyLiveEvents.objects.create(
                                    **serializer.validated_data)
                            tournament.events_hockey.add(event_object)
                        else:
                            print(serializer.errors)
            except KeyError:
                pass
    except Exception:
        pass


@shared_task
def send_request_endedmatch():
    try:
        with transaction.atomic():
            EndedMatch.objects.all().select_for_update().delete()
            url = "https://flashlive-sports.p.rapidapi.com/v1/events/list"
            querystring = {"timezone": "-4", "indent_days": "-1",
                           "locale": "en_INT", "sport_id": "1"}
            headers = {
                "X-RapidAPI-Key": "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
                "X-RapidAPI-Host": "flashlive-sports.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)
            parsed_data = response.json()
            try:
                for item in parsed_data['DATA']:
                    ended_match = EndedMatch.objects.filter(
                        tournamet_name=item['NAME'])
                    if ended_match.exists():
                        ended_match = ended_match.first()
                    else:
                        ended_match = EndedMatch.objects.create(
                            tournamet_name=item['NAME'],
                            tournament_imng=item['TOURNAMENT_IMAGE'],
                            stage_tyoe=item['TOURNAMENT_STAGE_TYPE']
                        )
                    for event in item['EVENTS']:
                        if event.get("STAGE_TYPE") == "FINISHED":
                            ended_match.event_id = event.get("EVENT_ID")
                            ended_match.round = event.get("ROUND")
                            ended_match.shortname_home = event.get(
                                "SHORTNAME_HOME")
                            ended_match.home_name = event.get("HOME_NAME")
                            ended_match.home_score_current = event.get(
                                "HOME_SCORE_CURRENT")
                            ended_match.home_score_part_1 = event.get(
                                "HOME_SCORE_PART_1")
                            ended_match.home_score_part_2 = event.get(
                                "HOME_SCORE_PART_2", '')
                            ended_match.home_images = event.get("HOME_IMAGES")
                            ended_match.shortname_away = event.get(
                                "SHORTNAME_AWAY")
                            ended_match.name_away = event.get("AWAY_NAME")
                            ended_match.away_score_current = event.get(
                                "AWAY_SCORE_CURRENT")
                            ended_match.away_score_full = event.get(
                                "AWAY_SCORE_FULL")
                            ended_match.away_score_part_1 = event.get(
                                "AWAY_SCORE_PART_1")
                            ended_match.away_score_part_2 = event.get(
                                "AWAY_SCORE_PART_2", '')
                            ended_match.away_images = event.get("AWAY_IMAGES")

                            ended_match.save()
            except KeyError:
                # Обработка ошибки KeyError
                pass
    except Exception:
        pass


@shared_task
def send_request_scheluded():
    try:
        with transaction.atomic():
            Scheduled.objects.all().select_for_update().delete()
            url = "https://flashlive-sports.p.rapidapi.com/v1/events/list"
            querystring = {"timezone": "-4", "indent_days": "-1",
                           "locale": "en_INT", "sport_id": "1"}
            headers = {
                "X-RapidAPI-Key": "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
                "X-RapidAPI-Host": "flashlive-sports.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)
            parsed_data = response.json()
            try:
                for item in parsed_data['DATA']:
                    scheduled_match = Scheduled.objects.filter(
                        tournamet=item['NAME'])
                    if scheduled_match.exists():
                        scheduled_match = scheduled_match.first()
                    else:
                        scheduled_match = Scheduled.objects.create(
                            tournamet=item['NAME'],
                            tournament_imng=item['TOURNAMENT_IMAGE'],
                            stage_type=item['TOURNAMENT_STAGE_TYPE']
                        )
                    for event in item['EVENTS']:
                        if event.get("STAGE_TYPE") == "SCHEDULED":
                            scheduled_match.event_id = event.get('EVENT_ID')
                            scheduled_match.start_time = event.get('START_TIME')
                            scheduled_match.start_utime = event.get('START_UTIME')
                            scheduled_match.shortname_home = event.get(
                                'SHORTNAME_HOME')
                            scheduled_match.home_name = event.get('HOME_NAME')
                            scheduled_match.home_images = event.get('HOME_IMAGES', '')
                            scheduled_match.shortname_away = event.get(
                                'SHORTNAME_AWAY')
                            scheduled_match.name_away = event.get('AWAY_NAME')
                            scheduled_match.away_images = event.get('AWAY_IMAGES', '')

                            scheduled_match.save()
            except KeyError:
                # Обработка ошибки KeyError
                pass
    except Exception:
        pass
