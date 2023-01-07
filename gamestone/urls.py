from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='gamestone/index.html')),
    path('suggest-game', TemplateView.as_view(template_name='gamestone/suggest_game.html')),
]
