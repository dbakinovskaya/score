from rest_framework import serializers

from .models import Seasons, Countries, Fixtures, Live, H2H, Leagues

class SeasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seasons
        fields = ['season_name', 'start_date', 'finish_date']

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['country_name', 'code', 'search']  

class LeaguesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leagues
        fields = ['league_name', 'country_id', 'seasons_id', 'type', 'current', 'search', 'last']    


class FixturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixtures
        fields = ['seasons_id', 'league_id', 'home_team_id', 'away_team_id', 'date']

class H2HSerializer(serializers.ModelSerializer):
    class Meta:
        model = H2H
        fields = ['team1_id', 'team2_id', 'date', 'fixture_id', 'league_id']

class LiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Live
        fields = ['fixture_id', 'home_score', 'away_score']                  