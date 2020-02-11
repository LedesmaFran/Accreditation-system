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
    if request.POST.get('cam_read'):
        id_user = request.POST.get('cam_read')
        person = participant.objects.get(id=id_user)
        if selected_event.registered.filter(id=id_user):
            selected_event.registered.remove(person)
            selected_event.accredit.add(person)
    return render(request, "qr.html", {'event': selected_event})


def ok(request, id_event, id_user):
    if not request.user.is_authenticated:
        return redirect('home')
    print(id_user)
    return render(request, "ok.html")


def accredited(request, id_event, id_user):
    if not request.user.is_authenticated:
        return redirect('home')
    person = participant.objects.get(id=id_user)
    return render(request, "accredited.html", {"person": person})

def no(request,id_event):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, "no.html")