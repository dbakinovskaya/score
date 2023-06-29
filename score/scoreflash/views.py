import requests
import http.client
import json

from django.views.generic import View, ListView
from django.http import JsonResponse
from django.shortcuts import render

from .models import Seasons, Countries, Leagues, Fixtures, H2H, Live


class SeasonsListView(ListView):
    model = Seasons
    template_name = 'seasons_list.html'
    context_object_name = 'seasons'

# тут сложность не нашел в документации get запрос


class CountriesListView(ListView):
    model = Countries
    template_name = 'countries_list.html'
    context_object_name = 'countries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")

        headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
        }

        conn.request("GET", "/countries", headers=headers)

        res = conn.getresponse()
        data = res.read()

        countries_data = json.loads(data.decode("utf-8"))
        context['countries_data'] = countries_data['response']

        return context
    
class LeaguesListView(ListView):
    model = Leagues
    template_name = 'leagues_list.html'
    context_object_name = 'leagues'

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.GET.get('country')
        season = self.request.GET.get('season')
        if country:
            queryset = queryset.filter(country=country)
        if season:
            queryset = queryset.filter(season=season)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # добавляем данные из API
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")

        headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
        }

        conn.request("GET", "/leagues", headers=headers)

        res = conn.getresponse()
        data = res.read()

        leagues_data = json.loads(data.decode("utf-8"))
        context['leagues_data'] = leagues_data['response']

        # добавляем данные о выбранных стране и сезоне
        context['selected_country'] = self.request.GET.get('country')
        context['selected_season'] = self.request.GET.get('season')

        return context
    
class FixturesListView(ListView):
    model = Fixtures 
    template_name = 'fixture_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        season_id = self.request.GET.get('season_id')
        league_id = self.request.GET.get('league_id')
        if season_id and league_id:
            queryset = queryset.filter(seasons_id=season_id, league_id=league_id)
    
        # Получение данных из базы данных
        fixtures_list = Fixtures.objects.all()
    
        # Добавление fixtures_list в словарь контекста
        self.extra_context = {'fixtures_list': fixtures_list}
    
        return queryset

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     season_id = self.request.GET.get('season_id')
    #     league_id = self.request.GET.get('league_id')
    #     if season_id and league_id:
    #         queryset = queryset.filter(seasons_id=season_id, league_id=league_id)
        
    #     # код для получения данных из API
    #     conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    #     headers = {
    #         'x-rapidapi-host': "v3.football.api-sports.io",
    #         'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    #     }
    #     conn.request("GET", "/fixtures?live=all", headers=headers)
    #     res = conn.getresponse()
    #     data = res.read()
        
    #     # обработка полученных данных
    #     fixtures_data = json.loads(data)
    #     fixtures_list = fixtures_data['response']
    #     for fixture in fixtures_list:
    #         # создание объектов модели Fixtures на основе полученных данных
    #         # и сохраняет в бд . если мы хотим чтобы просто выводидась в шаблон 
    #         Fixtures.objects.create (
    #             seasons_id = fixture['seasons']['id'],
    #             league_id=fixture['league']['id'],
    #             event_date=fixture['fixture']['date'],
    #             home_team_id=fixture['teams']['home']['id'],
    #             away_team_id=fixture['teams']['away']['id'],
               
    #         )
    #     return queryset

class H2HListView(ListView):
    model = H2H
    template_name = 'h2h.html'


    def process_h2h_data(self, data):
        h2h_data = {}
        for item in data:
            h2h_id = item.fixture_id_id
            date = item.date
            league = item.league_id_id
            home_team = item.team1_id_id
            away_team = item.team2_id_id
            # score = item.score
            # season = item.season
            h2h_data[f"{home_team} vs {away_team}"] = {
                'h2h': h2h_id,
                'date': date,
                'league': league,
                'fixture': f"{home_team} vs {away_team}",
                # 'season': season
            }
        return h2h_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        h2h_data = self.process_h2h_data(H2H.objects.all())  # Извлекайте данные из базы данных
        context['h2h_data'] = h2h_data
        return context

    # def process_h2h_data(self, data):
    #     h2h_data = {}
    #     json_data = json.loads(data)
    #     #fixtures = json_data['response']['fixtures']
    #     fixtures = json_data['response']
    #     for fixture in fixtures:
    #         h2h_id = fixture['fixture']['id']
    #         date = fixture['fixture']['date']
    #         league = fixture['league']['name']
    #         home_team = fixture['teams']['home']['name']
    #         away_team = fixture['teams']['away']['name']
    #         score = fixture['goals']['home'] + '-' + fixture['goals']['away']
    #         season = fixture['league']['season']
    #         h2h_data[f"{home_team} vs {away_team}"] = {
    #             'h2h': h2h_id,
    #             'date': date,
    #             'league': league,
    #             'fixture': f"{home_team} vs {away_team}",
    #             'season': season
    #      }
    #     return h2h_data

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    #     headers = {
    #         'x-rapidapi-host': "v3.football.api-sports.io",
    #         'x-rapidapi-key': "XxXxXxXxXxXxXxXxXxXxXxXx"
    #     }
    #     conn.request("GET", "/fixtures/headtohead?h2h=33-34", headers=headers)
    #     res = conn.getresponse()
    #     data = res.read().decode("utf-8")
    #     # process the data and store it in a variable called h2h_data
    #     h2h_data = self.process_h2h_data(data)
    #     context['h2h_data'] = h2h_data
    #     return context
    


class LiveView(View):
    def get(self, request):
        
        live_data = Live.objects.select_related('fixture_id').all()
        return render(request, 'live.html', {'live_data': live_data})    
    # def get(self, request):
    #     fixtures = Fixtures.objects.all()
    #     lives = Live.objects.all()
    #     return render(request, 'live.html', {'fixtures': fixtures, 'lives': lives})