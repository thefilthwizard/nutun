from django.shortcuts import render
from django.http.response import JsonResponse
from json import loads
from .models import ConfigItem, HistoryItem
import requests


def index(request):
    if request.method == "POST":
        return index_post(request)
    else:
        return index_get(request)


def index_get(request):
    ci = ConfigItem.objects.get(key="mapbox api key")
    context = {"mapbox_api_key": ci.value}
    return render(request, "weather/index_get.html", context)


def index_post(request):
    ci = ConfigItem.objects.get(key="open weather api key")
    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?lat={request.POST['lat']}&lon={request.POST['long']}&appid={ci.value}"
    )
    data = r.json()
    context = {
        "times": [
            {
                "description": item["weather"][0]["description"],
                "icon": f"http://openweathermap.org/img/wn/{item['weather'][0]['icon']}@4x.png",
                "dt_txt": item["dt_txt"],
                "dt": item["dt"],
                "location": request.POST["search-text"],
            }
            for item in data["list"]
        ],
    }
    return render(request, "weather/index_post.html", context)


def history(request):
    if request.method == "POST":
        return history_post(request)
    else:
        return history_get(request)


def history_post(request):
    data = loads(request.body.decode())
    hi = HistoryItem(**data)
    hi.save()
    return JsonResponse({"success": True})


def history_get(request):
    context = {"times": HistoryItem.objects.all().order_by("location", "dt").values()}
    return render(request, "weather/history_get.html", context)
