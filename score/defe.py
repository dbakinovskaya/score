# class LiveOfEventsViewSet(viewsets.ModelViewSet):
#     queryset = LiveOfEvents.objects.all()
#     serializer_class = LiveOfEventsSerializer

#     def list(self, request):
#         conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

#         headers = {
#             'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
#             'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
#         }

#         conn.request(
#             "GET", "/v1/events/live-list?timezone=-4&sport_id=1&locale=en_INT", headers=headers)

#         res = conn.getresponse()
#         data = res.read()

#         # Process the data as per your requirement
#         parsed_data = json.loads(data.decode("utf-8"))

#         # Create Event objects using the parsed data
#         event_data = parsed_data['event']
#         event = Event.objects.create(
#             events_id=event_data['events_id'],
#             strat_time=event_data['strat_time'],
#             start_utime=event_data['start_utime'],
#             stage_type=event_data['stage_type'],
#             merge_stage_type=event_data['merge_stage_type'],
#             stage=event_data['stage'],
#             sort=event_data['sort'],
#             visibale_run_rate=event_data['visibale_run_rate'],
#             live_mark=event_data['live_mark'],
#             has_lineps=event_data['has_lineps'],
#             stage_start_time=event_data['stage_start_time'],
#             game_time=event_data['game_time'],
#             playing_onset=event_data['playing_onset'],
#             recents_overs=event_data['recents_overs'],
#             short_name_home=event_data['short_name_home'],
#             HOME_PARTICIPANT_IDS=event_data['HOME_PARTICIPANT_IDS'],
#             HOME_PARTICIPANT_TYPES=event_data['HOME_PARTICIPANT_TYPES'],
#             home_name=event_data['home_name'],
#             home_par_name_one=event_data['home_par_name_one'],
#             home_event_par_id=event_data['home_event_par_id'],
#             home_goal_var=event_data['home_goal_var'],
#             home_score_current=event_data['home_score_current'],
#             home_score_part_1=event_data['home_score_part_1'],
#             home_images=event_data['home_images'],
#             imm=event_data['imm'],
#             imw=event_data['imw'],
#             imp=event_data['imp'],
#             ime=event_data['ime'],
#             short_name_away=event_data['short_name_away'],
#             away_par_ids=event_data['away_par_ids'],
#             away_par_types=event_data['away_par_types'],
#             away_name=event_data['away_name'],
#             away_par_name_one=event_data['away_par_name_one'],
#             away_event_par_id=event_data['away_event_par_id'],
#             away_goal_var=event_data['away_goal_var'],
#             away_score_current=event_data['away_score_current'],
#             away_score_full=event_data['away_score_full'],
#             away_score_part_1=event_data['away_score_part_1'],
#             away_images=event_data['away_images']
#         )

#         # Create LiveOfEvents object using the created Event object
        
#         live_event = LiveOfEvents.objects.create(
#         name=event_data['name'],
#         headers=event_data['headers'],
#         name_part_1=event_data['name_part_1'],
#         name_part_2=event_data['name_part_2'],
#         tournament_tamplete_id=event_data['tournament_tamplete_id'],
#         country_id=event_data['country_id'],
#         country_name=event_data['country_name'],
#         tournament_stage_id=event_data['tournament_stage_id'],
#         source_type=event_data['source_type'],
#         has_live_table=event_data['has_live_table'],
#         standing_info=event_data['standing_info'],
#         tamplate_id=event_data['tamplate_id'],
#         tournament_stage_type=event_data['tournament_stage_type'],
#         short_name=event_data['short_name'],
#         url=event_data['url'],
#         tourmanet_url=event_data['tourmanet_url'],
#         sort=event_data['sort'],
#         stage_count=event_data['stage_count'],
#         zkl=event_data['zkl'],
#         zku=event_data['zku'],
#         tournamet_season_id=event_data['tournamet_season_id'],
#         category_name=event_data['category_name'],
#         events=Events.objects.get(id=event_data['events']),
#         an=event_data['an'],
#         live_in_offer_book_id=event_data['live_in_offer_book_id'],
#         live_in_offer_status=event_data['live_in_offer_status']
#     )


#         return Response(data.decode("utf-8"), status=status.HTTP_200_OK)


start_time = ev['START_TIME']
start_utime = ev['START_UTIME']
stage_type = ev['STAGE_TYPE']
merge_stage_type = ev['MERGE_STAGE_TYPE']
stage = ev['STAGE']
sort = ev['SORT']
rounds = ev['ROUNDS']
visible_run_rate = ev['VISIBLE_RUN_RATE']
live_mark = ev['LIVE_MARK']
has_lineps = ev['HAS_LINEPS']
stage_start_time = ev['STAGE_START_TIME']
game_time = ev.get('GAME_TIME', None)
playing_on_sets = ev.get('PLAYING_ON_SETS', None)
recent_overs = ev.get('RECENT_OVERS', None)
shortname_away = ev['SHORTNAME_AWAY']
away_participant_ids = ev['AWAY_PARTICIPANT_IDS']
away_participant_types = ev['AWAY_PARTICIPANT_TYPES']
away_name = ev['AWAY_NAME']
away_participant_name_one = ev['AWAY_PARTICIPANT_NAME_ONE']
away_event_participant_id = ev['AWAY_EVENT_PARTICIPANT_ID']
away_goal_var = ev['AWAY_GOAL_VAR']
away_score_current = ev['AWAY_SCORE_CURRENT']
away_score_full = ev['AWAY_SCORE_FULL']
away_score_part_1 = ev.get('AWAY_SCORE_PART_1', None)
away_score_part_2 = ev.get('AWAY_SCORE_PART_2', None)
away_images = ev['AWAY_IMAGES']
imm = ev['IMM']
imw = ev['IMW']
imp = ev['IMP']
ime = ev['IME']
shortname_home = ev['SHORTNAME_HOME']
home_participant_ids = ev['HOME_PARTICIPANT_IDS']
home_participant_types = ev['HOME_PARTICIPANT_TYPES']
home_name = ev['HOME_NAME']
home_participant_name_one = ev['HOME_PARTICIPANT_NAME_ONE']
home_event_participant_id = ev['HOME_EVENT_PARTICIPANT_ID']
home_goal_var = ev['HOME_GOAL_VAR']
home_score_current = ev['HOME_SCORE_CURRENT']
home_score_part_1 = ev.get('HOME_SCORE_PART_1', None)
home_score_part_2 = ev.get('HOME_SCORE_PART_2', None)
home_images = ev['HOME_IMAGES']
tv_live_streaming = ev['TV_LIVE_STREAMING']
has_live_centre = ev['HAS_LIVE_CENTRE']
an = ev['AN']
bookmakers_with_live_in_offer = ev['BOOKMAKERS_WITH_LIVE_IN_OFFER']
live_in_offer_bookmaker_id = ev['LIVE_IN_OFFER_BOOKMAKER_ID']
live_in_offer_status = ev['LIVE_IN_OFFER_STATUS']
score_chance_away = ev['SCORE_CHANCE_AWAY']
if event_id:    
                    query += "'" + event_id + "', "
                else:
                    query += "NULL, "

                if start_time:
                    query += "'" + str(start_time) + "', "
                else:
                    query += "NULL, "

                if start_utime:
                    query += "'" +str(start_utime) + "', "
                else:
                    query += "NULL, "

                if stage_type:
                    query += "'" + stage_type + "', "
                else:
                    query += "NULL, "

                if merge_stage_type:
                    query += "'" + merge_stage_type + "', "
                else:
                    query += "NULL, "

                if stage:
                    query += "'" + stage + "', "
                else:
                    query += "NULL, "

                if sort:
                    query += "'" + sort + "', "
                else:
                    query += "NULL, "

                if rounds:
                    query += "'" + rounds + "', "
                else:
                    query += "NULL, "

                if visible_run_rate:
                    query += "'" + visible_run_rate + "', "
                else:
                    query += "NULL, "

                if live_mark:
                    query += "'" + live_mark + "', "
                else:
                    query += "NULL, "

                if has_lineps:
                    query += "'" + str(has_lineps) + "', "
                else:
                    query += "NULL, "

                if stage_start_time:
                    query += "'" + str(stage_start_time) + "', "
                else:
                    query += "NULL, "

                if game_time:
                    query += "'" + game_time + "', "
                else:
                    query += "NULL, "

                if playing_on_sets:
                    query += "'" + playing_on_sets + "', "
                else:
                    query += "NULL, "

                if recent_overs:
                    query += "'" + recent_overs + "', "
                else:
                    query += "NULL, "

                if shortname_away:
                    query += "'" + shortname_away + "', "
                else:
                    query += "NULL, "

                if away_participant_ids:
                    query += "'" + str(away_participant_ids) + "', "
                else:
                    query += "NULL, "

                if away_participant_types:
                    query += "'" + str(away_participant_types) + "', "
                else:
                    query += "NULL, "

                if away_name:
                    query += "'" + away_name + "', "
                else:
                    query += "NULL, "

                if away_participant_name_one:
                    query += "'" + away_participant_name_one + "', "
                else:
                    query += "NULL, "

                if away_event_participant_id:
                    query += "'" + away_event_participant_id + "', "
                else:
                    query += "NULL, "

                if away_goal_var:
                    query += "'" + away_goal_var + "', "
                else:
                    query += "NULL, "

                if away_score_current:
                    query += "'" + away_score_current + "', "
                else:
                    query += "NULL, "

                if away_score_full:
                    query += "'" + away_score_full + "', "
                else:
                    query += "NULL, "

                if away_score_part_1:
                    query += "'" + away_score_part_1 + "', "
                else:
                    query += "NULL, "

                if away_score_part_2:
                    query += "'" + away_score_part_2 + "', "
                else:
                    query += "NULL, "

                if away_images:
                    query += "'" + str(away_images) + "', "
                else:
                    query += "NULL, "

                if imm:
                    query += "'" + imm + "', "
                else:
                    query += "NULL, "

                if imw:
                    query += "'" + imw + "', "
                else:
                    query += "NULL, "

                if imp:
                    query += "'" + imp + "', "
                else:
                    query += "NULL, "

                if ime:
                    query += "'" + ime + "', "
                else:
                    query += "NULL, "

                if shortname_home:
                    query += "'" + shortname_home + "', "
                else:
                    query += "NULL, "

                if home_participant_ids:
                    query += "'" + str(home_participant_ids) + "', "
                else:
                    query += "NULL, "

                if home_participant_types:
                    query += "'" +str(home_participant_types) + "', "
                else:
                    query += "NULL, "

                if home_name:
                    query += "'" + home_name + "', "
                else:
                    query += "NULL, "

                if home_participant_name_one:
                    query += "'" + home_participant_name_one + "', "
                else:
                    query += "NULL, "

                if home_event_participant_id:
                    query += "'" + home_event_participant_id + "', "
                else:
                    query += "NULL, "

                if home_goal_var:
                    query += "'" + home_goal_var + "', "
                else:
                    query += "NULL, "

                if home_score_current:
                    query += "'" + home_score_current + "', "
                else:
                    query += "NULL, "

                if home_score_part_1:
                    query += "'" + home_score_part_1 + "', "
                else:
                    query += "NULL, "

                if home_score_part_2:
                    query += "'" + home_score_part_2 + "', "
                else:
                    query += "NULL, "

                if home_images:
                    query += "'" +str(home_images) + "', "
                else:
                    query += "NULL, "

                if tv_live_streaming:
                    query += "'" + str(tv_live_streaming) + "', "
                else:
                    query += "NULL, "

                if has_live_centre:
                    query += "'" + str(has_live_centre) + "', "
                else:
                    query += "NULL, "

                if an:
                    query += "'" + an + "', "
                else:
                    query += "NULL, "

                if bookmakers_with_live_in_offer:
                    query += "'" + str(bookmakers_with_live_in_offer) + "', "
                else:
                    query+= "NULL, "
                if live_in_offer_bookmaker_id:
                    query += "'" + str(live_in_offer_bookmaker_id) + "', "
                else:
                    query += "NULL, "

                if live_in_offer_status:
                    query += "'" + str(live_in_offer_status) + "', "
                else:
                    query += "NULL, "

                if score_chance_away:
                    query += "'" + score_chance_away + "', "
                else:
                    query += "NULL, "

                # Remove the last comma and add the closing parenthesis
                query = query[:-2] + ")"


# cursor.execute("INSERT INTO scoreflash_events (event_id, start_time, start_utime, stage_type, merge_stage_type, stage, sort, rounds, visible_run_rate, live_mark, has_lineps, stage_start_time, game_time, playing_on_sets, recent_overs, shortname_away, away_participant_ids, away_participant_types, away_name, away_participant_name_one, away_event_participant_id, away_goal_var, away_score_current, away_score_full, away_score_part_1, away_score_part_2, away_images, imm, imw, imp, ime, shortname_home, home_participant_ids, home_participant_types, home_name, home_participant_name_one, home_event_participant_id, home_goal_var, home_score_current, home_score_part_1, home_score_part_2, home_images, tv_live_streaming, has_live_centre, an, bookmakers_with_live_in_offer, live_in_offer_bookmaker_id, live_in_offer_status, score_chance_away) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                    # event_id, start_time, start_utime,
                    # stage_type, merge_stage_type, stage, sort, rounds,
                    # visible_run_rate, live_mark, has_lineps, stage_start_time,
                    # game_time, playing_on_sets, recent_overs, shortname_away, away_participant_ids,
                    # away_participant_types, away_name, away_participant_name_one, away_event_participant_id,
                    # away_goal_var, away_score_current, away_score_full, away_score_part_1,
                    # away_score_part_2, away_images, imm, imw, imp,
                    # ime, shortname_home, home_participant_ids,
                    # home_participant_types, home_name,
                    # home_participant_name_one,
                    # home_event_participant_id,
                    # home_goal_var, home_score_current,
                    # home_score_part_1, home_score_part_2,
                    # home_images, tv_live_streaming,
                    # has_live_centre, an,
                    # bookmakers_with_live_in_offer,
                    # live_in_offer_bookmaker_id,
                    # live_in_offer_status,
                    # score_chance_away))