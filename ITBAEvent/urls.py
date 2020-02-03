from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_events, name='show_events'),
]