from django.shortcuts import render
from ITBAEvent.models import Event
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def qr_reader(request, id_event):
    if request.POST.get('cam_read'):
        print(request.POST.get('cam_read'))

    selected_event = Event.objects.get(id=id_event)
    return render(request, "qr.html", {'event': selected_event})
