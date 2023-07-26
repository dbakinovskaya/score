from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import LiveOfEventsViewSet


router = DefaultRouter()

router.register('live-events', LiveOfEventsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]