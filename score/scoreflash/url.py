from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import EventDetails, EventIdViewSet


router = DefaultRouter()

# router.register('live-events', LiveOfEventsViewSet)
router.register(r'event-ids', EventIdViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/events/live/', EventIdViewSet.as_view({'get': 'list'})),
    path('live-events/event-details/<str:live_event_id>/',
         EventDetails.as_view(), name='event-details'),
]
