from . import views
from django.urls import path

urlpatterns = [
    path('<id_event>/', views.qr_reader, name='qr_reader'),
    path('<id_event>/<id_user>/ok/',views.ok, name='ok'),
    path('<id_event>/<id_user>/accredited/',views.accredited, name='accredited'),
    path('<id_event>/no/',views.no, name='no')
    ]