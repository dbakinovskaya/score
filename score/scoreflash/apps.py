from django.apps import AppConfig
import asyncio


class ScoreflashConfig(AppConfig):
    name = 'scoreflash'

    def ready(self):
        from .views import EventIdViewSet

        event_id_viewset = EventIdViewSet()
        event_id_viewset.start_scheduling()
