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


class EventId(models.Model):
    live_event_id = models.TextField(null=True)


class Tournament(models.Model):
    name = models.TextField(null=True)
    tournament_stage_type = models.TextField(null=True)
    tournament_imng = models.TextField(null=True)
    TOURNAMENT_TEMPLATE_ID = models.TextField(null=True)
    TOURNAMENT_IMAGE = models.URLField(null=True)


class Events(models.Model):
    tournament = models.ForeignKey(
        Tournament, related_name='events', on_delete=models.CASCADE, null=True)
    event_id = models.TextField(null=True)
    start_time = models.TextField(null=True)
    start_utime = models.TextField(null=True)
    game_time = models.TextField(null=True)
    short_name_away = models.TextField(null=True)
    away_name = models.TextField(null=True)
    away_score_current = models.TextField(null=True)
    away_score_part_1 = models.TextField(null=True)
    away_score_part_2 = models.TextField(null=True)
    away_images = models.URLField(null=True)
    short_name_home = models.TextField(null=True)
    home_name = models.TextField(null=True)
    home_score_current = models.TextField(null=True)
    home_score_part_1 = models.TextField(null=True)
    home_score_part_2 = models.TextField(null=True)
    home_images = models.URLField(null=True)


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
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)


class TournamentHockey(models.Model):
    name = models.TextField(null=True)
    tournament_stage_type = models.TextField(null=True)
    tournament_imng = models.TextField(null=True)
    TOURNAMENT_TEMPLATE_ID = models.TextField(null=True)
    TOURNAMENT_IMAGE = models.URLField(null=True)


class HockeyLiveEvents(models.Model):
    tournament = models.ForeignKey(
        TournamentHockey, related_name='events_hockey', on_delete=models.CASCADE, null=True)
    EVENT_ID = models.TextField(null=True)
    START_TIME = models.TextField(null=True)
    START_UTIME = models.TextField(null=True)
    STAGE_TYPE = models.TextField(null=True)
    MERGE_STAGE_TYPE = models.TextField(null=True)
    STAGE = models.TextField(null=True)
    SORT = models.TextField(null=True)
    LIVE_MARK = models.TextField(null=True)
    HAS_LINEPS = models.TextField(null=True)
    STAGE_START_TIME = models.TextField(null=True)
    GAME_TIME = models.TextField(null=True)
    PLAYING_ON_SETS = models.TextField(null=True)
    RECENT_OVERS = models.TextField(null=True)
    SHORTNAME_HOME = models.TextField(null=True)
    HOME_PARTICIPANT_IDS = models.TextField(null=True)
    HOME_PARTICIPANT_TYPES = models.TextField(null=True)
    HOME_NAME = models.TextField(null=True)
    HOME_PARTICIPANT_NAME_ONE = models.TextField(null=True)
    HOME_EVENT_PARTICIPANT_ID = models.TextField(null=True)
    HOME_GOAL_VAR = models.TextField(null=True)
    HOME_SCORE_CURRENT = models.TextField(null=True)
    HOME_SCORE_PART_1 = models.TextField(null=True)
    HOME_SCORE_PART_2 = models.TextField(null=True)
    HOME_SCORE_PART_3 = models.TextField(null=True)
    HOME_IMAGES = models.TextField(null=True)
    SHORTNAME_AWAY = models.TextField(null=True)
    AWAY_PARTICIPANT_IDS = models.TextField(null=True)
    AWAY_PARTICIPANT_TYPES = models.TextField(null=True)
    AWAY_NAME = models.TextField(null=True)
    AWAY_PARTICIPANT_NAME_ONE = models.TextField(null=True)
    AWAY_EVENT_PARTICIPANT_ID = models.TextField(null=True)
    AWAY_GOAL_VAR = models.TextField(null=True)
    AWAY_SCORE_CURRENT = models.TextField(null=True)
    AWAY_SCORE_FULL = models.TextField(null=True)
    AWAY_SCORE_PART_1 = models.TextField(null=True)
    AWAY_SCORE_PART_2 = models.TextField(null=True)
    AWAY_SCORE_PART_3 = models.TextField(null=True)
    AWAY_IMAGES = models.TextField(null=True)
