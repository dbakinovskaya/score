from django.urls import path
from .views import MatchesView

urlpatterns = [
    path('matches/', MatchesView.as_view(), name='match_list'),
]