from django.http import HttpResponse
from django.shortcuts import render
from .models import Trolley

# Create your views here.


def homePage(request):
    trollies = Trolley.objects.all()

    return render(
        request,
        "counter/index.html",
        {"trollies": trollies}
    )

def addTrolley(request):
    return HttpResponse("Hello World, this is the addTrolley page")

def trolleyDetail(request):
    return HttpResponse("Hello World, this is the trolley deetail page!")

def statistics(request):
    return HttpResponse("hello World, this is the statistics page!!")