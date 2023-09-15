from django.db import models


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
    red_cards_home = models.TextField(null=True)
    red_cards_away = models.TextField(null=True)
    yellow_cards_home = models.TextField(null=True)
    yellow_cards_away = models.TextField(null=True)


class EventId(models.Model):
    live_event_id = models.OneToOneField(
        Events, on_delete=models.CASCADE, null=True)


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
    HOME_SCORE_PART_2 = models.TextField(null=True, blank=True)
    HOME_SCORE_PART_3 = models.TextField(null=True, blank=True)
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
    AWAY_SCORE_PART_2 = models.TextField(null=True, blank=True)
    AWAY_SCORE_PART_3 = models.TextField(null=True, blank=True)
    AWAY_IMAGES = models.TextField(null=True)


class EndedMatch(models.Model):
    tournamet_name = models.TextField(null=True)
    tournament_stage_type = models.TextField(null=True)
    tournament_imng = models.TextField(null=True)
    event_id = models.TextField(null=True)
    stage_tyoe = models.TextField(null=True)
    round = models.TextField(null=True)
    shortname_home = models.TextField(null=True)
    home_name = models.TextField(null=True)
    home_score_current = models.TextField(null=True)
    home_score_part_1 = models.TextField(null=True)
    home_score_part_2 = models.TextField(null=True)
    home_images = models.TextField(null=True)
    shortname_away = models.TextField(null=True)
    name_away = models.TextField(null=True)
    away_score_current = models.TextField(null=True)
    away_score_full = models.TextField(null=True)
    away_score_part_1 = models.TextField(null=True)
    away_score_part_2 = models.TextField(null=True)
    away_images = models.TextField(null=True)


class Scheduled(models.Model):
    tournament = models.TextField(null=True)
    tournament_stage_type = models.TextField(null=True)
    tournament_imng = models.TextField(null=True)
    event_id = models.TextField(null=True)
    start_time = models.TextField(null=True)
    start_utime = models.TextField(null=True)
    shortname_home = models.TextField(null=True)
    home_name = models.TextField(null=True)
    home_images = models.TextField(null=True)
    shortname_away = models.TextField(null=True)
    name_away = models.TextField(null=True)
    away_images = models.TextField(null=True)


class All(models.Model):
    tournamet_name = models.TextField(null=True)
    tournament_stage_type = models.TextField(null=True)
    tournament_imng = models.TextField(null=True)
    event_id = models.TextField(null=True)
    stage_type = models.TextField(null=True)
    round = models.TextField(null=True)
    shortname_home = models.TextField(null=True)
    home_name = models.TextField(null=True)
    home_score_current = models.TextField(null=True)
    home_score_part_1 = models.TextField(null=True)
    home_score_part_2 = models.TextField(null=True)
    home_images = models.TextField(null=True)
    shortname_away = models.TextField(null=True)
    name_away = models.TextField(null=True)
    away_score_current = models.TextField(null=True)
    away_score_full = models.TextField(null=True)
    away_score_part_1 = models.TextField(null=True)
    away_score_part_2 = models.TextField(null=True)
    away_images = models.TextField(null=True)


class AllHockey(models.Model):
    tournamet_name = models.TextField(null=True)
    tournament_stage_type = models.TextField(null=True)
    tournament_imng = models.TextField(null=True)
    event_id = models.TextField(null=True)
    stage_type = models.TextField(null=True)
    round = models.TextField(null=True)
    shortname_home = models.TextField(null=True)
    home_name = models.TextField(null=True)
    home_score_current = models.TextField(null=True)
    home_score_part_1 = models.TextField(null=True)
    home_score_part_2 = models.TextField(null=True)
    home_score_part_3 = models.TextField(null=True)
    home_images = models.TextField(null=True)
    shortname_away = models.TextField(null=True)
    name_away = models.TextField(null=True)
    away_score_current = models.TextField(null=True)
    away_score_full = models.TextField(null=True)
    away_score_part_1 = models.TextField(null=True)
    away_score_part_2 = models.TextField(null=True)
    away_score_part_3 = models.TextField(null=True)
    away_images = models.TextField(null=True)


class ScheduledHockey(models.Model):
    tournament = models.TextField(null=True)
    tournament_stage_type = models.TextField(null=True)
    tournament_imng = models.TextField(null=True)
    event_id = models.TextField(null=True)
    start_time = models.TextField(null=True)
    start_utime = models.TextField(null=True)
    shortname_home = models.TextField(null=True)
    home_name = models.TextField(null=True)
    home_images = models.TextField(null=True)
    shortname_away = models.TextField(null=True)
    name_away = models.TextField(null=True)
    away_images = models.TextField(null=True)


class EndedHockey(models.Model):
    tournament_stage_type = models.TextField(null=True)
    tournament_imng = models.TextField(null=True)
    event_id = models.TextField(null=True)
    stage_tyoe = models.TextField(null=True)
    round = models.TextField(null=True)
    shortname_home = models.TextField(null=True)
    home_name = models.TextField(null=True)
    home_score_current = models.TextField(null=True)
    home_score_part_1 = models.TextField(null=True)
    home_score_part_2 = models.TextField(null=True)
    home_score_part_3 = models.TextField(null=True)
    home_images = models.TextField(null=True)
    shortname_away = models.TextField(null=True)
    name_away = models.TextField(null=True)
    away_score_current = models.TextField(null=True)
    away_score_full = models.TextField(null=True)
    away_score_part_1 = models.TextField(null=True)
    away_score_part_2 = models.TextField(null=True)
    away_score_part_3 = models.TextField(null=True)
    away_images = models.TextField(null=True)
