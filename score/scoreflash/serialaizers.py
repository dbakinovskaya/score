from rest_framework import serializers
from .models import (Sport, NumberOfSportEvents, Bookmaker,
                     Outcome, Market, Group, Events, LiveOfEvents, EventId, Tournament,
                       HockeyLiveEvents,TournamentHockey,Cards)


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
    home_images = serializers.ListField(allow_null=True, required=False)
    away_images = serializers.ListField(allow_null=True, required=False)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        home_images = representation.get('home_images', [])
        home_images_string = ''.join(home_images)
        representation['home_images'] = home_images_string

        away_images = representation.get('away_images', [])
        away_images_string = ''.join(away_images)
        representation['away_images'] = away_images_string

        return representation

    class Meta:
        model = Events
        fields = ['event_id', 'start_time', 'start_utime', 'game_time', 'short_name_away',
                  'away_name', 'away_score_current', 'away_score_part_1', 'short_name_home',
                  'home_name', 'home_score_current', 'home_score_part_1', 'home_images', 'away_images']


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
        fields = ['id', 'name', 'tournament_stage_type', 'tournament_imng',
                  'TOURNAMENT_TEMPLATE_ID', 'TOURNAMENT_IMAGE', 'events']



class HockeyLiveEventsSerializer(serializers.ModelSerializer):
    HOME_IMAGES = serializers.ListField(allow_null=True, required=False)
    AWAY_IMAGES = serializers.ListField(allow_null=True, required=False)
    HOME_SCORE_PART_3 = serializers.CharField(allow_null=True, required=False)
    AWAY_SCORE_PART_3 = serializers.CharField(allow_null=True, required=False)
    HOME_SCORE_PART_2 = serializers.CharField(allow_null=True, required=False)
    AWAY_SCORE_PART_2 = serializers.CharField(allow_null=True, required=False)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        home_images = representation.get('HOME_IMAGES', [])
        home_images_string = ''.join(home_images)
        representation['HOME_IMAGES'] = home_images_string

        away_images = representation.get('AWAY_IMAGES', [])
        away_images_string = ''.join(away_images)
        representation['AWAY_IMAGES'] = away_images_string

        return representation
    
    class Meta:
        model = HockeyLiveEvents
        fields = '__all__'

class TournamentHockeySerializer(serializers.ModelSerializer):
    events_hockey = HockeyLiveEventsSerializer(many=True)

    class Meta:
        model = TournamentHockey
        fields = ['id', 'name', 'tournament_stage_type', 'tournament_imng', 'TOURNAMENT_TEMPLATE_ID', 'TOURNAMENT_IMAGE', 'events_hockey']


class CardsSerializer(serializers.ModelSerializer):
    away_yellow = serializers.CharField(allow_null=True, required=False)
    away_red = serializers.CharField(allow_null=True, required=False)
    home_yellow = serializers.CharField(allow_null=True, required=False)
    home_red = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = Cards
        fields = '__all__'