from django.http import HttpResponse

# Create your views here.


def homePage(request):
    return HttpResponse("Hello world, this is the home page!")

def addTrolley(request):
    return HttpResponse("Hello World, this is the addTrolley page")

def trolleyDetail(request):
    return HttpResponse("Hello World, this is the trolley deetail page!")

def statistics(request):
    return HttpResponse("hello World, this is the statistics page!!")