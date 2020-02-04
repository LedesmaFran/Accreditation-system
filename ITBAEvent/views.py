from .models import Event
from datetime import datetime, timedelta
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.

def show_events(request):
    if request.GET.get('id'):
        id_event = request.GET.get('id')
        select_event = Event.objects.get(id=id_event)
        return render(request, 'events.html', {'select_event': select_event})

    if request.GET.get('accredit'):
        id_number = request.GET.get('accredit')
        return redirect('qr_reader',id_number)

    if request.GET.get('today'):
        events = Event.objects.filter(start_time__date=datetime.today())
        if events is None:
            return render(request, 'events.html')
    elif request.GET.get('all'):
        events = Event.objects.all()
    else:
        events = Event.objects.filter(start_time__date=datetime.today()).filter(end_time__range=(datetime.now(), datetime.now() + timedelta(days=1)))
    return render(request, 'events.html', {'events': events})
