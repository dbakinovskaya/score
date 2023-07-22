import requests
import http.client
import json

from django.views.generic import View, ListView
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_400_BAD_REQUEST

from .models import Seasons, Countries, Leagues, Fixtures, H2H, Live
from .serialaizers import (SeasonsSerializer, CountriesSerializer, 
LeaguesSerializer,LiveSerializer,H2HSerializer, FixturesSerializer)


class SeasonsViewSet(viewsets.ModelViewSet):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer

# тут сложность не нашел в документации get запрос


class CountriesViewSet(viewsets.ViewSet):
    def list(self, request):
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")

        headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
        }

        conn.request("GET", "/countries", headers=headers)

        res = conn.getresponse()
        data = res.read()

        countries_data = json.loads(data.decode("utf-8"))

        serializer = CountriesSerializer(countries_data['response'], many=True)

        return Response(serializer.data)
    
class LeaguesViewSet(viewsets.ViewSet):
    def list(self, request):
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")

        headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528"
        }

        conn.request("GET", "/leagues", headers=headers)

        res = conn.getresponse()
        data = res.read()

        leagues_data = json.loads(data.decode("utf-8"))

        serializer = LeaguesSerializer(leagues_data['response'], many=True)

        return Response(serializer.data)
    
class FixturesViewSet(viewsets.ViewSet):
    queryset = Fixtures.objects.all()
    serializer_class = FixturesSerializer

    def list(self, request):
        queryset = self.queryset
        season_id = request.GET.get('season_id')
        league_id = request.GET.get('league_id')
        if season_id and league_id:
            queryset = queryset.filter(seasons_id=season_id, league_id=league_id)

        # код для получения данных из API
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
        }
        conn.request("GET", "/fixtures?live=all", headers=headers)
        res = conn.getresponse()
        data = res.read()

        # обработка полученных данных
        fixtures_data = json.loads(data)
        fixtures_list = fixtures_data['response']
        for fixture in fixtures_list:
            # создание объектов модели Fixtures на основе полученных данных
            Fixtures.objects.create(
                seasons_id=fixture['seasons']['id'],
                league_id=fixture['league']['id'],
                event_date=fixture['fixture']['date'],
                home_team_id=fixture['teams']['home']['id'],
                away_team_id=fixture['teams']['away']['id'],
            )

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        fixture = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(fixture)
        return Response(serializer.data)

class H2HViewSet(viewsets.ViewSet):
    queryset = H2H.objects.all()
    serializer_class = H2HSerializer

    def list(self, request):
        queryset = self.queryset

        # код для получения данных из API
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
        }
        conn.request("GET", "/fixtures/headtohead?h2h=33-34", headers=headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")

        # обработка полученных данных
        h2h_data = self.process_h2h_data(data)
        for fixture in h2h_data.values():
            # создание объектов модели H2H на основе полученных данных
            H2H.objects.create(
                h2h_id=fixture['h2h'],
                date=fixture['date'],
                league=fixture['league'],
                fixture=fixture['fixture'],
                season=fixture['season']
            )

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        h2h = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(h2h)
        return Response(serializer.data)

    def process_h2h_data(self, data):
        h2h_data = {}
        json_data = json.loads(data)
        fixtures = json_data['response']
        for fixture in fixtures:
            h2h_id = fixture['fixture']['id']
            date = fixture['fixture']['date']
            league = fixture['league']['name']
            home_team = fixture['teams']['home']['name']
            away_team = fixture['teams']['away']['name']
            score = fixture['goals']['home'] + '-' + fixture['goals']['away']
            season = fixture['league']['season']
            h2h_data[f"{home_team} vs {away_team}"] = {
                'h2h': h2h_id,
                'date': date,
                'league': league,
                'fixture': f"{home_team} vs {away_team}",
                'season': season
            }
        return h2h_data


class LiveViewSet(viewsets.ViewSet):
    def list(self, request):
        conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
            'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
        }

        conn.request("GET", "/fixtures/live", headers=headers)

        res = conn.getresponse()
        data = res.read()

        live_data = Live.objects.select_related('fixture_id').all()
        serializer = LiveSerializer(live_data, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
            'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
        }

        conn.request("GET", "/fixtures/live", headers=headers)

        res = conn.getresponse()
        data = res.read()

        live_data = Live.objects.select_related('fixture_id').get(id=pk)
        serializer = LiveSerializer(live_data)
        return Response(serializer.data)

    def create(self, request):
        serializer = LiveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
            'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
        }

        conn.request("GET", "/fixtures/live", headers=headers)

        res = conn.getresponse()
        data = res.read()

        live_data = Live.objects.select_related('fixture_id').get(id=pk)
        serializer = LiveSerializer(live_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
            'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
        }

        conn.request("GET", "/fixtures/live", headers=headers)

        res = conn.getresponse()
        data = res.read()

        live_data = Live.objects.select_related('fixture_id').get(id=pk)
        live_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_live_data(self):
        conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
            'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
        }

        conn.request("GET", "/fixtures/live", headers=headers)

        res = conn.getresponse()
        data = res.read()

        return data.decode("utf-8")
    