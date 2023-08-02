from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import LiveOfEventsViewSet, EventDetails, EventIdViewSet


router = DefaultRouter()

router.register('live-events', LiveOfEventsViewSet)
router.register(r'event-ids', EventIdViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
     path('live-events/event-details/<str:event_id>/', EventDetails.as_view(), name='event-details'),
]