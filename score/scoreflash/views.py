
import http.client


from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


from .models import LiveOfEvents, Events
from .serialaizers import LiveOfEventsSerializer, EventsSerializer
import http.client


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class LiveOfEventsViewSet(viewsets.ModelViewSet):
    queryset = LiveOfEvents.objects.all()
    serializer_class = LiveOfEventsSerializer

    def list(self, request):
        conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
            'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
        }

        conn.request("GET", "/v1/events/live-list?timezone=-4&sport_id=1&locale=en_INT", headers=headers)

        res = conn.getresponse()
        data = res.read()

        # Process the data as per your requirement
        # For example, you can parse the JSON response and return it as a response

        return Response(data.decode("utf-8"), status=status.HTTP_200_OK)


def h2h(event_id):
    conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
        'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
    }

    conn.request("GET", f"/v1/events/h2h?locale=en_INT&event_id={event_id}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def events_statistic(event_id):
    conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
        'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
    }

    conn.request("GET", f"/v1/events/statistics?event_id={event_id}&locale=en_INT", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


def events_start_lineps(event_id):

    conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
        'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
    }

    conn.request("GET", f"/v1/events/lineups?event_id={event_id}&locale=en_INT", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def odds(event_id):
    conn = http.client.HTTPSConnection("flashlive-sports.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "c68d4d6ac2mshe98277d48f502dbp188062jsn10858273d528",
        'X-RapidAPI-Host': "flashlive-sports.p.rapidapi.com"
    }

    conn.request("GET", f"/v1/events/odds?event_id={event_id}&locale=en_INT", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))    


class EventDetails(APIView):
    def get(self, request, event_id):
        event_id = get_object_or_404(Events, events_id=event_id)

        # Вызываем функции, передавая значение event_id
        h2h_data = h2h(event_id)
        events_statistic_data = events_statistic(event_id)
        events_start_lineps_data = events_start_lineps(event_id)
        odds_data = odds(event_id)

        # Выводим данные на экран
        print('Event ID:', event_id)
        print('H2H Data:', h2h_data)
        print('Events Statistic Data:', events_statistic_data)
        print('Events Start Lineps Data:', events_start_lineps_data)
        print('Odds Data:', odds_data)

        # Создаем JSON-ответ
        response = {
            'event_id': event_id,
            'h2h_data': h2h_data,
            'events_statistic_data': events_statistic_data,
            'events_start_lineps_data': events_start_lineps_data,
            'odds_data': odds_data
        }

        # Возвращаем JSON-ответ
        return Response(response)
