from django.urls import path, include
from .views import SeasonsViewSet,CountriesViewSet, LeaguesViewSet, FixturesViewSet,H2HViewSet, LiveViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'seasons', SeasonsViewSet)
router.register(r'fixtures', FixturesViewSet)
router.register(r'api/leagues', LeaguesViewSet, basename='leagues')
router.register(r'api/countries', CountriesViewSet, basename='countries')
router.register(r'h2h', H2HViewSet)
router.register(r'live', LiveViewSet)

urlpatterns = [
    path('', include(router.urls)),
]