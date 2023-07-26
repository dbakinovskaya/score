
import http.client


from rest_framework import viewsets, status
from rest_framework.response import Response


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
