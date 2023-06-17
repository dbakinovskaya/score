from django.shortcuts import render
from django.contrib.auth.views import login
from django.views.generic import View
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
from .models import Match

class MatchesView(View):
    def get(self, request):
        url = 'https://example.com/matches'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        matches = []

        for match in soup.find_all('div', class_='match'):
            home_team = match.find('div', class_='home-team').text.strip()
            away_team = match.find('div', class_='away-team').text.strip()
            home_odds = match.find('div', class_='home-odds').text.strip()
            away_odds = match.find('div', class_='away-odds').text.strip()
            draw_odds = match.find('div', class_='draw-odds').text.strip()

            # Создаем запись в базе данных
            Match.objects.create(
                home_team=home_team,
                away_team=away_team,
                home_odds=home_odds,
                away_odds=away_odds,
                draw_odds=draw_odds
            )

            # Добавляем данные в список для отправки в ответе
            matches.append({
                'home_team': home_team,
                'away_team': away_team,
                'home_odds': home_odds,
                'away_odds': away_odds,
                'draw_odds': draw_odds
            })

        context = {'matches': matches}
        return render(request, 'score/mathes.html', context)