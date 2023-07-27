from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import LiveOfEventsViewSet, EventDetails


router = DefaultRouter()

router.register('live-events', LiveOfEventsViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('live-events/event-details/<str:event_id>/', EventDetails.as_view(), name='event-details'),
]