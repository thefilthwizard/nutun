from django.urls import path

from . import views

app_name = "weather"

urlpatterns = [
    path("", views.index, name="index"),
    path("history", views.history, name="history"),
    path("about", views.about, name="about"),
]
