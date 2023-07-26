from rest_framework import serializers
from .models import (Sport, NumberOfSportEvents, Bookmaker,Outcome, Market, Group,Events,LiveOfEvents)

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['sport_id', 'name']

class NumberOfSportEventsSerializer(serializers.ModelSerializer):
    sport = SportSerializer()

    class Meta:
        model = NumberOfSportEvents
        fields = ['sport', 'events_count', 'events_count_live', 'is_popular', 'sports_name']

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
        fields = ['id', 'bookmaker', 'odd_cell_third_move', 'odd_cell_third_value', 'odds_available', 'locale']

class GroupSerializer(serializers.ModelSerializer):
    outcomes = OutcomeSerializer()

    class Meta:
        model = Group
        fields = ['id', 'group_name', 'outcomes', 'locale']


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'   

class LiveOfEventsSerializer(serializers.ModelSerializer):
    events = EventsSerializer()  # использование ранее созданного сериализатора для связанной модели

    class Meta:
        model = LiveOfEvents
        fields = '__all__'             
