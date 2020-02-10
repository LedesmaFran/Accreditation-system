from django.shortcuts import render
from ITBAEvent.models import Event, participant
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, HttpResponse, reverse
from django.http import JsonResponse


# Create your views here.
@csrf_exempt
def qr_reader(request, id_event):
    selected_event = Event.objects.get(id=id_event)
    if not request.user.is_authenticated:
        return redirect('home')

    return render(request, "qr.html", {'event': selected_event})


def check_data(request):
    id_user = request.POST.get('cam_read')
    print(id_user)
    id_event = request.POST.get('event')
    print(id_event)
    event = Event.objects.get(id=id_event)
    if event.registered.filter(id=id_user):
        person = participant.objects.filter(id=id_user)
        print(person)
        return JsonResponse("ok")
    else:
        return HttpResponse("fallo")