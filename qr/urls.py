from . import views
from django.urls import path

urlpatterns = [
    path('<id_event>/', views.qr_reader, name='qr_reader'),
    ]