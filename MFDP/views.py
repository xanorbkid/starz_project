from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    services = Services.objects.all()[:6]

    context={
        'services':services,
    }
    return render(request, 'index.html', context)


def about(request):

    executives = Executive_Team.objects.all()[:3]

    context ={
        'executives':executives
    }
    return render(request, 'about-us.html', context)

def service(request):
    services = Services.objects.all()

    context={
        'services':services,
    }
    return render(request, 'service.html', context)

def team(request):
    teams = Team.objects.all()

    context ={
        'teams':teams,
    }
    return render(request, 'team.html', context)

def team_exe(request):
    executives = Executive_Team.objects.all()

    context ={
        'executives':executives,
    }
    return render(request, 'team2.html', context)


def contact(request):
    return render(request, 'contactus.html')

def mission(request):
    return render(request, 'mission & vision.html')