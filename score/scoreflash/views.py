from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render
import requests
from .models import Match

headers = {
    'X-RapidAPI-Key': 'YOUR_API_KEY',
    'X-RapidAPI-Host': 'flashlive-sports.p.rapidapi.com'
}

class MatchesView(View):
    def get(self, request):
        url = 'https://flashlive-sports.p.rapidapi.com/scores/live.json'
        params = {
            'l': '1', # Код локали (1 - международный)
            'tz': 'Europe/Moscow' # Часовой пояс
        }
        response = requests.get(url, headers=headers, params=params) # Добавляем заголовки и параметры запроса
        data = response.json()

        events = data['events'] # Получаем список спортивных событий

        for event in events:
            # Создаем объект Match и сохраняем его в базу данных
            match = Match.objects.create(
                home_team=event['home_team']['name'],
                away_team=event['away_team']['name'],
                home_odds=event['home_team']['odds'],
                away_odds=event['away_team']['odds'],
                draw_odds=event['draw_odds'],
            )

        context = {'events': events}
        return render(request, 'score/mathes.html', context)
    def post(self, request):
        match_id = request.POST.get('match_id')
        new_score = request.POST.get('new_score')

        # Обновляем счет матча в базе данных
        match = Match.objects.get(id=match_id)
        match.score = new_score
        match.save()

        return JsonResponse({'success': True})
