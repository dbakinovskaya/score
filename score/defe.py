from django.shortcuts import render, get_object_or_404
from .models import Event

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})


3. В файле urls.py вашего Django-приложения добавьте маршрут для обработки запросов к отдельному окну:

python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Остальные маршруты
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]
