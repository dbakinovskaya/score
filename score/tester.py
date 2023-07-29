python
from rest_framework.response import Response

def my_view(request):
    # Ваш код обработки запроса

    # Проверка каждого значения на None и создание списка полей и значений для SQL-запроса
    fields = []
    values = []
    if event_id is not None:
        fields.append("event_id")
        values.append(event_id)
    if start_time is not None:
        fields.append("start_time")
        values.append(start_time)
    # Добавьте проверку для остальных полей

    # Выполнение SQL-запроса и сохранение данных в базу данных
    db_conn = sqlite3.connect('db.sqlite3')
    cursor = db_conn.cursor()
    if fields:
        fields_str = ", ".join(fields)
        values_str = ", ".join(["?"] * len(values))
        query = f"INSERT INTO scoreflash_events ({fields_str}) VALUES ({values_str})"
        cursor.execute(query, values)
        db_conn.commit()
    db_conn.close()

    # Создание и возвращение объекта ответа
    return Response("Data saved successfully")

    fields = []
    values = []
    if event_id is not None:
        fields.append("event_id")
        values.append(event_id)
    if start_time is not None:
        fields.append("start_time")
        values.append(start_time)
    if start_utime is not None:
        fields.append("start_utime")
        values.append(start_utime)
    if stage_type is not None:
        fields.append("stage_type")
        values.append(stage_type)
    if merge_stage_type is not None:
        fields.append("merge_stage_type")
        values.append(merge_stage_type)
    if stage is not None:
        fields.append("stage")
        values.append(stage)
    if sort is not None:
        fields.append("sort")
        values.append(sort)
    if rounds is not None:
        fields.append("rounds")
        values.append(rounds)
    if visible_run_rate is not None:
        fields.append("visible_run_rate")
        values.append(visible_run_rate)
    if live_mark is not None:
        fields.append("live_mark")
        values.append(live_mark)
    if has_lineps is not None:
        fields.append("has_lineps")
        values.append(has_lineps)
    if stage_start_time is not None:
        fields.append("stage_start_time")
        values.append(stage_start_time)
    if game_time is not None:
        fields.append("game_time")
        values.append(game_time)
    if playing_on_sets is not None:
        fields.append("playing_on_sets")
        values.append(playing_on_sets)
    if recent_overs is not None:
        fields.append("recent_overs")
        values.append(recent_overs)
    if shortname_away is not None:
        fields.append("shortname_away")
        values.append(shortname_away)
    if away_participant_ids is not None:
        fields.append("away_participant_ids")
        values.append(away_participant_ids)
    if away_participant_types is not None:
        fields.append("away_participant_types")
        values.append(away_participant_types)
    if away_name is not None:
        fields.append("away_name")
        values.append(away_name)
    if away_participant_name_one is not None:
        fields.append("away_participant_name_one")
        values.append(away_participant_name_one)
    if away_event_participant_id is not None:
        fields.append("away_event_participant_id")
        values.append(away_event_participant_id)
    if away_goal_var is not None:
        fields.append("away_goal_var")
        values.append(away_goal_var)
    if away_score_current is not None:
        fields.append("away_score_current")
        values.append(away_score_current)
    if away_score_full is not None:
        fields.append("away_score_full")
        values.append(away_score_full)
    if away_score_part_1 is not None:
        fields.append("away_score_part_1")
        values.append(away_score_part_1)
    if away_score_part_2 is not None:
        fields.append("away_score_part_2")
        values.append(away_score_part_2)
    if away_images is not None:
        fields.append("away_images")
        values.append(away_images)
    if imm is not None:
        fields.append("imm")
        values.append(imm)
    if imw is not None:
        fields.append("imw")
        values.append(imw)
    if imp is not None:
        fields.append("imp")
        values.append(imp)
    if ime is not None:
        fields.append("ime")
        values.append(ime)
    if shortname_home is not None:
        fields.append("shortname_home")
        values.append(shortname_home)
    if home_participant_ids is not None:
        fields.append("home_participant_ids")
        values.append(home_participant_ids)
    if home_participant_types is not None:
        fields.append("home_participant_types")
        values.append(home_participant_types)
    if home_name is not None:
        fields.append("home_name")
        values.append(home_name)
    if home_participant_name_one is not None:
        fields.append("home_participant_name_one")
        values.append(home_participant_name_one)
    if home_event_participant_id is not None:
        fields.append("home_event_participant_id")
        values.append(home_event_participant_id)
    if home_goal_var is not None:
        fields.append("home_goal_var")
        values.append(home_goal_var)
    if home_score_current is not None:
        fields.append("home_score_current")
        values.append(home_score_current)
    if home_score_full is not None:
        fields.append("home_score_full")
        values.append(home_score_full)
    if home_score_part_1 is not None:
        fields.append("home_score_part_1")
        values.append(home_score_part_1)
    if home_score_part_2 is not None:
        fields.append("home_score_part_2")
        values.append(home_score_part_2)
    if home_images is not None:
        fields.append("home_images")
        values.append(home_images)
    if tv_live_streaming is not None:
        fields.append("tv_live_streaming")
        values.append(tv_live_streaming)
    if has_live_centre is not None:
        fields.append("has_live_centre")
        values.append(has_live_centre)
    if an is not None:
        fields.append("an")
        values.append(an)
    if bookmakers_with_live_in_offer is not None:
        fields.append("bookmakers_with_live_in_offer")
        values.append(bookmakers_with_live_in_offer)
    if live_in_offer_bookmaker_id is not None:
        fields.append("live_in_offer_bookmaker_id")
        values.append(live_in_offer_bookmaker_id)
    if live_in_offer_status is not None:
        fields.append("live_in_offer_status")
        values.append(live_in_offer_status)
    if '%' + score_chance_away + '%' is not None:
        fields.append("score_chance_away")
        values.append('%' + score_chance_away + '%')

    # Выполнение SQL-запроса и сохранение данных в базу данных
    db_conn = sqlite3.connect('db.sqlite3')
    cursor = db_conn.cursor()
    if fields:
        fields_str = ", ".join(fields)
        values_str = ", ".join(["?"] * len(values))
        query = f"INSERT INTO scoreflash_events ({fields_str}) VALUES ({values_str})"
        cursor.execute(query, values)
        db_conn.commit()
    db_conn.close()    
