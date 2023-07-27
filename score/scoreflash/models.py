from django.db import models


class Sport(models.Model):
    sport_id = models.IntegerField()
    name = models.CharField(max_length=255, blank=False, null=True)


class NumberOfSportEvents(models.Model):
    sport_id = models.ForeignKey(Sport, on_delete=models.CASCADE)
    events_count = models.IntegerField()
    events_count_live = models.IntegerField()
    is_popular = models.IntegerField()
    sports_name = models.CharField(max_length=255, blank=False, null=True)


class Bookmaker(models.Model):
    bookmaker_id = models.IntegerField()
    bookmaker_name = models.CharField(max_length=100)
    locale = models.CharField(max_length=255, blank=False, null=True)


class Outcome(models.Model):
    odds_label_second = models.CharField(max_length=10)
    odds_label_third = models.CharField(max_length=10)
    locale = models.CharField(max_length=255, blank=False, null=True)


class Market(models.Model):
    bookmaker = models.ForeignKey(Bookmaker, on_delete=models.CASCADE)
    odd_cell_third_move = models.CharField(max_length=1)
    odd_cell_third_value = models.FloatField()
    odds_available = models.IntegerField()
    locale = models.CharField(max_length=255, blank=False, null=True)


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    outcomes = models.ForeignKey(Outcome, on_delete=models.CASCADE, null=True)
    locale = models.CharField(max_length=255, blank=False, null=True)


class Period(models.Model):
    odds_stage = models.CharField(max_length=100)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    locale = models.CharField(max_length=255, blank=False, null=True)


class BettingType(models.Model):
    betting_type = models.CharField(max_length=100)
    periods = models.ForeignKey(Period, on_delete=models.CASCADE)
    locale = models.CharField(max_length=255, blank=False, null=True)


class Match(models.Model):
    betting_type = models.ForeignKey(BettingType, on_delete=models.CASCADE)
    locale = models.CharField(max_length=255, blank=False, null=True)



class Teams(models.Model):
    team_id = models.IntegerField()
    layout = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    gender_id = models.IntegerField()
    country_id = models.IntegerField()
    country_name = models.CharField(max_length=100)
    image_path = models.URLField()  # вот надо проверить
    imm = models.CharField(max_length=100)
    image_width = models.IntegerField()
    image_id = models.CharField(max_length=100)
    ime = models.CharField(max_length=100)
    image_table_path = models.URLField()
    name = models.CharField(max_length=100)
    type_id = models.IntegerField()
    type_name = models.CharField(max_length=100)
    tab = models.CharField(max_length=10)
    parent_name = models.CharField(max_length=100)
    actual_tournament_type = models.CharField(max_length=100)
    actual_tournament_stage_id = models.CharField(max_length=100)
    actual_tournament_season_id = models.CharField(max_length=100)
    team_id_id = models.CharField(max_length=100)
    team_participant_type = models.IntegerField()
    team_image = models.ImageField(null=True)
    team_name = models.CharField(max_length=100)
    sport_id = models.ForeignKey(Sport, on_delete=models.CASCADE)


class Events(models.Model):
    events_id = models.CharField(max_length=100)
    strat_time = models.IntegerField()
    start_utime = models.IntegerField()
    stage_type = models.CharField(max_length=100)
    merge_stage_type = models.CharField(max_length=100)
    stage = models.CharField(max_length=100)
    sort = models.CharField(max_length=100)
    visibale_run_rate = models.IntegerField()
    live_mark = models.CharField(max_length=100)
    has_lineps = models.IntegerField()
    stage_start_time = models.IntegerField()
    game_time = models.CharField(max_length=100, null=True)
    playing_onset = models.CharField(max_length=100, null=True)
    recents_overs = models.CharField(max_length=100, null=True)
    short_name_home = models.CharField(max_length=100)
    HOME_PARTICIPANT_IDS = models.TextField(null=True)
    HOME_PARTICIPANT_TYPES = models.TextField(null=True)
    home_name = models.CharField(max_length=100)
    home_par_name_one = models.CharField(max_length=100)
    home_event_par_id = models.CharField(max_length=100)
    home_goal_var = models.IntegerField()
    home_score_current = models.CharField(max_length=100)
    home_score_part_1 = models.CharField(max_length=100)
    home_images = models.URLField()
    imm = models.CharField(max_length=100)
    imw = models.CharField(max_length=100)
    imp = models.CharField(max_length=100)
    ime = models.CharField(max_length=100)
    short_name_away = models.CharField(max_length=100)
    away_par_ids = models.TextField(null=True)
    away_par_types = models.TextField(null=True)
    away_name = models.CharField(max_length=100)
    away_par_name_one = models.CharField(max_length=100)
    away_event_par_id = models.CharField(max_length=100)
    away_goal_var = models.IntegerField()
    away_score_current = models.CharField(max_length=100)
    away_score_full = models.IntegerField()
    away_score_part_1 = models.CharField(max_length=100)
    away_images = models.URLField()


class LiveOfEvents(models.Model):
    name = models.CharField(max_length=100)
    headers = models.CharField(max_length=100)
    name_part_1 = models.CharField(max_length=100)
    name_part_2 = models.CharField(max_length=100)
    tournament_tamplete_id = models.CharField(max_length=100)
    country_id = models.IntegerField()
    country_name = models.CharField(max_length=100)
    tournament_stage_id = models.CharField(max_length=100)
    source_type = models.IntegerField()
    has_live_table = models.IntegerField()
    standing_info = models.IntegerField()
    tamplate_id = models.CharField(max_length=100)
    tournament_stage_type = models.IntegerField()
    short_name = models.CharField(max_length=100)
    url = models.URLField()
    tourmanet_url = models.URLField()
    sort = models.CharField(max_length=100)
    stage_count = models.IntegerField()
    zkl = models.CharField(max_length=100)
    zku = models.CharField(max_length=100)
    tournamet_season_id = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)
    events = models.ForeignKey(Events, on_delete=models.CASCADE)
    an = models.CharField(max_length=100)
    live_in_offer_book_id = models.IntegerField()
    live_in_offer_status = models.IntegerField()

# class GroupStatics(models.Model):
#     event = models.ForeignKey(Events, on_delete=models.CASCADE)
#     group_label = models.CharField(max_length=50)

#     def __str__(self):
#         return self.group_label

# class Item(models.Model):
#     group = models.ForeignKey(GroupStatics, on_delete=models.CASCADE)
#     incident_name = models.CharField(max_length=50)
#     value_home = models.CharField(max_length=50)
#     value_away = models.CharField(max_length=50)

#     def __str__(self):
#         return self.incident_name
    

# class Statics(models.Model):
#     event = models.ForeignKey(Events, on_delete=models.CASCADE)
#     group = models.ForeignKey(GroupStatics, on_delete=models.CASCADE)
#     element = models.ForeignKey(Item, on_delete=models.CASCADE)


# class H2H(models.Model):
#     event_id  = models.ForeignKey(Events, on_delete=models.CASCADE)



# class DetailMatch(models.Model):
#     event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
#     h2h = models.ForeignKey(H2H, on_delete=models.CASCADE)
#     event_statics = models.ForeignKey(Statics,on_delete=models.CASCADE)
    # book = 
    # event_start_lineps = 