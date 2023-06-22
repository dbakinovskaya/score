from django.urls import path
from .views import (CountriesListView, LeaguesListView,
                    FixturesListView,H2HListView,LiveView)

urlpatterns = [
    path('fixtures/', FixturesListView.as_view(), name='fixtures_list'),
    path('h2h/', H2HListView.as_view(), name='h2h'),
    path('live/', LiveView.as_view(), name='live'),
]