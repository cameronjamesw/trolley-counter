from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name="home"),
    path("add/", views.addTrolley, name="add trolley"),
    path("<int:pk>/detail/", views.trolleyDetail, name="detail"),
    path("stats/", views.statistics, name="stats"),
]
