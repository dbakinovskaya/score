class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TourmanetSerializer

    def list(self, request):
        async def send_request():
            with transaction.atomic():  # Используем транзакцию
                Tournament.objects.all().delete()  # Удаление всех существующих турниров
                Events.objects.all().delete()  # Удаление всех существующих событий

                conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")
                headers = {
                    'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
                    'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
                }
                conn.request(
                    "GET", "/v1/events/live-list?timezone=-4&sport_id=1&locale=en_INT", headers=headers)
                res = conn.getresponse()
                data = res.read()
                parsed_data = json.loads(data.decode("utf-8"))
                for item in parsed_data['DATA']:
                    tournament = Tournament()
                    tournament.name = item['NAME']
                    tournament.tournament_stage_type = item['TOURNAMENT_STAGE_TYPE']
                    tournament.tournament_imng = item['TOURNAMENT_IMAGE']
                    tournament.TOURNAMENT_TEMPLATE_ID = item['TOURNAMENT_TEMPLATE_ID']

                    for event in item['EVENTS']:
                        data = {
                            'event_id': event['EVENT_ID'],
                            'start_time': event['START_TIME'],
                            'start_utime': event['START_UTIME'],
                            'game_time': event['GAME_TIME'],
                            'short_name_away': event['SHORTNAME_AWAY'],
                            'away_name': event['AWAY_NAME'],
                            'away_score_current': event['AWAY_SCORE_CURRENT'],
                            'away_score_part_1': event['AWAY_SCORE_PART_1'],
                            'away_score_part_2': event.get('AWAY_SCORE_PART_2', ''),
                            'away_images': event.get('AWAY_IMAGES', ''),
                            'short_name_home': event['SHORTNAME_HOME'],
                            'home_name': event['HOME_NAME'],
                            'home_score_current': event['HOME_SCORE_CURRENT'],
                            'home_score_part_1': event['HOME_SCORE_PART_1'],
                            'home_score_part_2': event.get('HOME_SCORE_PART_2', ''),
                            'home_images': event.get('HOME_IMAGES', '')
                        }
                        serializer = EventsSerializer(data=data)
                        if serializer.is_valid():
                            event_object = serializer.create(serializer.validated_data)
                            tournament.events.add(event_object)
                        else:
                            print(serializer.errors)

                    tournament.save()

        async def schedule_request():
            while True:
                await send_request()  # Выполняем запрос
                await asyncio.sleep(5)  # Подождать 5 секунд

        def start_scheduling():
            loop = asyncio.new_event_loop()  # Создаем новый цикл событий
            asyncio.set_event_loop(loop)  # Устанавливаем его как текущий
            loop.run_until_complete(schedule_request())  # Запускаем цикл событий

        start_scheduling()


        javascript
function updateData() {
  // Отправить AJAX-запрос для получения новых данных
  $.ajax({
    url: 'your-api-endpoint',
    method: 'GET',
    success: function(response) {
      // Очистить предыдущие данные
      $('#data-container').empty();
      
      // Отобразить новые данные
      response.forEach(function(item) {
        $('#data-container').append('<p>' + item.name + '</p>');
      });
    },
    complete: function() {
      // Запустить обновление данных через 7 секунд
      setTimeout(updateData, 7000);
    }
  });
}

// Запустить обновление данных
updateData();