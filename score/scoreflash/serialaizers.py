from rest_framework import serializers
from .models import (Sport, NumberOfSportEvents, Bookmaker,
                     Outcome, Market, Group, Events, LiveOfEvents, EventId, Tournament)


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['sport_id', 'name']


class NumberOfSportEventsSerializer(serializers.ModelSerializer):
    sport = SportSerializer()

    class Meta:
        model = NumberOfSportEvents
        fields = ['sport', 'events_count',
                  'events_count_live', 'is_popular', 'sports_name']


class BookmakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmaker
        fields = ['bookmaker_id', 'bookmaker_name', 'locale']


class OutcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outcome
        fields = ['id', 'odds_label_second', 'odds_label_third', 'locale']


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ['id', 'bookmaker', 'odd_cell_third_move',
                  'odd_cell_third_value', 'odds_available', 'locale']


class GroupSerializer(serializers.ModelSerializer):
    outcomes = OutcomeSerializer()

    class Meta:
        model = Group
        fields = ['id', 'group_name', 'outcomes', 'locale']


class EventsSerializer(serializers.ModelSerializer):
    # away_images = serializers.URLField()
    # home_images = serializers.URLField()
    class Meta:
        model = Events
        fields = ['event_id', 'start_time', 'start_utime', 'game_time', 'short_name_away',
                  'away_name', 'away_score_current', 'away_score_part_1', 'short_name_home',
                  'home_name', 'home_score_current', 'home_score_part_1', 'home_images','away_images']


class LiveOfEventsSerializer(serializers.ModelSerializer):
    # использование ранее созданного сериализатора для связанной модели
    events = EventsSerializer()

    class Meta:
        model = LiveOfEvents
        fields = '__all__'


class EventLiveIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventId
        fields = '__all__'


class TournamentSerializer(serializers.ModelSerializer):
    events = EventsSerializer(many=True)

    class Meta:
        model = Tournament
        fields = ['id', 'name', 'tournament_stage_type', 'tournament_imng', 'TOURNAMENT_TEMPLATE_ID', 'TOURNAMENT_IMAGE', 'events']