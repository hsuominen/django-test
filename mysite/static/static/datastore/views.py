# Create your views here.

from django.shortcuts import render

from datastore.models import acquisition

# def index(request):
#     latest_acq_list = acquisition.objects.all().order_by('-acqdatetime')[:5]
#     context = {'latest_acq_list': latest_acq_list}
#     return render(request, 'datastore/index.html', context)

def index(request):
    return render(request, 'datastore/index.html', {"acquisitions": acquisition.objects.all()})

def detail(request, acq_id):
    return HttpResponse("You're looking at acquisition %s." % acq_id)

def coordinates(request, acq_id):
    return HttpResponse("You're looking at the coordinates of acquisition %s." % acq_id)

def values(request, acq_id):
    return HttpResponse("You're looking at the values of acquisition %s." % acq_id)