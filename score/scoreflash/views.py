
import http.client
import sqlite3
import json

from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


from .models import LiveOfEvents, Events
from .serialaizers import LiveOfEventsSerializer, EventsSerializer
import http.client


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
            for ev in event['EVENTS']:
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
                obj = Events()
                try:
                    if event_id:
                        obj.event_id=event_id
                        obj.save()  
                except Exception as e:
                    print("Ошибка при сохранении obj:event", str(e)) 
                try:                 
                    if start_time:
                        obj.start_time = start_time
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:start_time", str(e))
                try:            
                    if start_utime:
                        obj.start_utime = start_utime
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:start_utime", str(e))
                try:             
                    if stage_type:
                        obj.stage_type = stage_type
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:stage_type", str(e)) 
                try:          
                    if merge_stage_type:
                        obj.merge_stage_type = merge_stage_type
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:merge_stage_type", str(e)) 
                try:           
                    if stage:
                        obj.stage = stage
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:stage", str(e))
                try:            
                    if sort:
                        obj.sort = sort
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:sort", str(e))
                try:           
                    if rounds:
                        obj.rounds = rounds
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:rounds", str(e))
                try:           
                    if visible_run_rate:
                        obj.visible_run_rate = visible_run_rate
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:visible_run_rate", str(e))
                try:            
                    if live_mark:
                        obj.live_mark = live_mark
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:", str(e))
                try:    
                    if has_lineps:
                        obj.has_lineps = has_lineps
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:live_mark", str(e))
                try:        
                    if stage_start_time:
                        obj.stage_start_time = stage_start_time
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:stage_start_time", str(e))
                try:                
                    if game_time:
                        obj.game_time = game_time
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:game_time", str(e))
                try:           
                    if playing_on_sets:
                        obj.playing_on_sets = playing_on_sets
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:playing_on_sets", str(e))
                try:           
                    if recent_overs:
                        obj.recent_overs = recent_overs
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj: recent_overs", str(e))
                try:           
                    if shortname_away:
                        obj.shortname_away = shortname_away
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:shortname_away", str(e))
                try:            
                    if away_participant_ids:
                        obj.away_participant_ids = away_participant_ids
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:away_participant_ids", str(e)) 
                try:          
                    if away_participant_types:
                        obj.away_participant_types = away_participant_types
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:away_participant_types", str(e))
                try:           
                    if away_name:
                        obj.away_name = away_name
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:away_name", str(e))
                try:           
                    if away_participant_name_one:
                        obj.away_participant_name_one = away_participant_name_one
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:away_participant_name_one", str(e))
                try:           
                    if away_event_participant_id:
                        obj.away_event_participant_id = away_event_participant_id
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:away_event_participant_id", str(e))
                try:           
                    if away_goal_var:
                        obj.away_goal_var = away_goal_var
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:away_goal_var", str(e))
                try:            
                    if away_score_current:
                        obj.away_score_current = away_score_current
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:away_score_current", str(e))
                try:            
                    if away_score_full:
                        obj.away_score_full = away_score_full
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:away_score_full", str(e))
                try:           
                    if away_score_part_1:
                        obj.away_score_part_1 = away_score_part_1
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:away_score_part_1", str(e))
                try:            
                    if away_score_part_2:
                        obj.away_score_part_2 = away_score_part_2
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:away_score_part_2", str(e))
                try:            
                    if away_images:
                        obj.away_images = away_images
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:away_images", str(e))
                try:            
                    if imm:
                        obj.imm = imm
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:imm", str(e))
                try:           
                    if imw:
                        obj.imw = imw
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj: imw", str(e))
                try:           
                    if imp:
                        obj.imp = imp
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:imp", str(e)) 
                try:           
                    if ime:
                        obj.ime = ime
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:ime", str(e))
                try:            
                    if shortname_home:
                        obj.shortname_home = shortname_home
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:shortname_home", str(e))
                try:            
                    if home_participant_ids:
                        obj.home_participant_ids = home_participant_ids
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении objhome_participant_ids:", str(e))
                try:            
                    if home_participant_types:
                        obj.home_participant_types = home_participant_types
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:home_participant_types", str(e))
                try:           
                    if home_name:
                        obj.home_name = home_name
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:home_name", str(e))
                try:            
                    if home_participant_name_one:
                        obj.home_participant_name_one = home_participant_name_one
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:home_participant_name_one", str(e))
                try:       
                    if home_event_participant_id:
                        obj.home_event_participant_id = home_event_participant_id
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:home_event_participant_id", str(e))
                try:           
                    if home_goal_var:
                        obj.home_goal_var = home_goal_var
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:home_goal_var", str(e))
                try:            
                    if home_score_current:
                        obj.home_score_current = home_score_current
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:home_score_current", str(e))
                try:            
                    if home_score_part_1:
                        obj.home_score_part_1 = home_score_part_1
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj: home_score_part_1", str(e))
                try:           
                    if home_score_part_2:
                        obj.home_score_part_2 = home_score_part_2
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:home_score_part_2", str(e))
                try:            
                    if home_images:
                        obj.home_images = home_images
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:home_images", str(e))
                try:            
                    if tv_live_streaming:
                        obj.tv_live_streaming = tv_live_streaming
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:tv_live_streaming", str(e))
                try:            
                    if has_live_centre:
                        obj.has_live_centre = has_live_centre
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:has_live_centre", str(e))
                try:           
                    if an:
                        obj.an = an
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:an", str(e))
                try:           
                    if bookmakers_with_live_in_offer:
                        obj.bookmakers_with_live_in_offer = bookmakers_with_live_in_offer
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj: bookmakers_with_live_in_offer", str(e))
                try:            
                    if live_in_offer_bookmaker_id:
                        obj.live_in_offer_bookmaker_id = live_in_offer_bookmaker_id
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:live_in_offer_bookmaker_id", str(e))
                try:           
                    if live_in_offer_status:
                        obj.live_in_offer_status = live_in_offer_status
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:live_in_offer_status", str(e))
                try:            
                    if score_chance_away:
                        obj.score_chance_away = score_chance_away
                        obj.save()
                except Exception as e:
                    print("Ошибка при сохранении obj:score_chance_away", str(e))        
               

                # Выполнение SQL-запроса и сохранение данных в базу данных
    
                return Response(data)

        # Create Event objects using the parsed data
        # event_data = parsed_data
        # event = Events.objects.create(
        #     events_id=event_data['events_id'],
        #     strat_time=event_data['strat_time'],
        #     start_utime=event_data['start_utime'],
        #     stage_type=event_data['stage_type'],
        #     merge_stage_type=event_data['merge_stage_type'],
        #     stage=event_data['stage'],
        #     sort=event_data['sort'],
        #     visibale_run_rate=event_data['visibale_run_rate'],
        #     live_mark=event_data['live_mark'],
        #     has_lineps=event_data['has_lineps'],
        #     stage_start_time=event_data['stage_start_time'],
        #     game_time=event_data['game_time'],
        #     playing_onset=event_data['playing_onset'],
        #     recents_overs=event_data['recents_overs'],
        #     short_name_home=event_data['short_name_home'],
        #     HOME_PARTICIPANT_IDS=event_data['HOME_PARTICIPANT_IDS'],
        #     HOME_PARTICIPANT_TYPES=event_data['HOME_PARTICIPANT_TYPES'],
        #     home_name=event_data['home_name'],
        #     home_par_name_one=event_data['home_par_name_one'],
        #     home_event_par_id=event_data['home_event_par_id'],
        #     home_goal_var=event_data['home_goal_var'],
        #     home_score_current=event_data['home_score_current'],
        #     home_score_part_1=event_data['home_score_part_1'],
        #     home_images=event_data['home_images'],
        #     imm=event_data['imm'],
        #     imw=event_data['imw'],
        #     imp=event_data['imp'],
        #     ime=event_data['ime'],
        #     short_name_away=event_data['short_name_away'],
        #     away_par_ids=event_data['away_par_ids'],
        #     away_par_types=event_data['away_par_types'],
        #     away_name=event_data['away_name'],
        #     away_par_name_one=event_data['away_par_name_one'],
        #     away_event_par_id=event_data['away_event_par_id'],
        #     away_goal_var=event_data['away_goal_var'],
        #     away_score_current=event_data['away_score_current'],
        #     away_score_full=event_data['away_score_full'],
        #     away_score_part_1=event_data['away_score_part_1'],
        #     away_images=event_data['away_images']
        # )

        # Create LiveOfEvents object using the created Event object

        # live_event = LiveOfEvents.objects.create(
        #     name=event_data['name'],
        #     headers=event_data['headers'],
        #     name_part_1=event_data['name_part_1'],
        #     name_part_2=event_data['name_part_2'],
        #     tournament_tamplete_id=event_data['tournament_tamplete_id'],
        #     country_id=event_data['country_id'],
        #     country_name=event_data['country_name'],
        #     tournament_stage_id=event_data['tournament_stage_id'],
        #     source_type=event_data['source_type'],
        #     has_live_table=event_data['has_live_table'],
        #     standing_info=event_data['standing_info'],
        #     tamplate_id=event_data['tamplate_id'],
        #     tournament_stage_type=event_data['tournament_stage_type'],
        #     short_name=event_data['short_name'],
        #     url=event_data['url'],
        #     tourmanet_url=event_data['tourmanet_url'],
        #     sort=event_data['sort'],
        #     stage_count=event_data['stage_count'],
        #     zkl=event_data['zkl'],
        #     zku=event_data['zku'],
        #     tournamet_season_id=event_data['tournamet_season_id'],
        #     category_name=event_data['category_name'],
        #     events=Events.objects.get(id=event_data['events']),
        #     an=event_data['an'],
        #     live_in_offer_book_id=event_data['live_in_offer_book_id'],
        #     live_in_offer_status=event_data['live_in_offer_status']
        # )

        # return Response(data.decode("utf-8"), status=status.HTTP_200_OK)


def h2h(event_id):
    conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
        'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
    }

    conn.request(
        "GET", f"/v1/events/h2h?locale=en_INT&event_id={event_id}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def events_statistic(event_id):
    conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
        'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
    }

    conn.request(
        "GET", f"/v1/events/statistics?event_id={event_id}&locale=en_INT", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def events_start_lineps(event_id):

    conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
        'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
    }

    conn.request(
        "GET", f"/v1/events/lineups?event_id={event_id}&locale=en_INT", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def odds(event_id):
    conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
        'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
    }

    conn.request(
        "GET", f"/v1/events/odds?event_id={event_id}&locale=en_INT", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


class EventDetails(APIView):
    def get(self, request, event_id):
        event_id = get_object_or_404(Events, event_id=event_id)

        # Вызываем функции, передавая значение event_id
        h2h_data = h2h(event_id)
        events_statistic_data = events_statistic(event_id)
        events_start_lineps_data = events_start_lineps(event_id)
        odds_data = odds(event_id)

        # Выводим данные на экран
        print('Event ID:', event_id)
        print('H2H Data:', h2h_data)
        print('Events Statistic Data:', events_statistic_data)
        print('Events Start Lineps Data:', events_start_lineps_data)
        print('Odds Data:', odds_data)

        # Создаем JSON-ответ
        response = {
            'event_id': event_id,
            'h2h_data': h2h_data,
            'events_statistic_data': events_statistic_data,
            'events_start_lineps_data': events_start_lineps_data,
            'odds_data': odds_data
        }

        # Возвращаем JSON-ответ
        return Response(response)
