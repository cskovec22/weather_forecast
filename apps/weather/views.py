from datetime import datetime, timedelta
import requests

from django.shortcuts import render

from apps.weather import forms


TOTAL_SECONDS_IN_3_DAYS = 3 * 24 * 60 * 60


def get_city_coordinates(city):
    """Получить координаты города."""

    url_geocoding = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city,
        "count": 1,
        "language": "ru"
    }
    response = requests.get(url=url_geocoding, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get("results"):
            return (
                data["results"][0]["latitude"],
                data["results"][0]["longitude"],
                data["results"][0]["timezone"]
            )
        else:
            raise ValueError("Город не найден.")
    else:
        raise requests.RequestException(
            "Не удалось получить координаты города."
        )


def get_weather(latitude, longitude, timezone):
    """Получить погоду по координатам места."""

    url_meteo = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone,
        "forecast_days": 4,
        "hourly": [
            "temperature_2m",
            "wind_speed_10m",
            "wind_direction_10m",
            "precipitation"
        ]
    }
    response = requests.get(url=url_meteo, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise requests.RequestException("Не удалось получить данные о погоде.")


def get_formatted_weather(weather):
    """Преобразовать данные о прогнозе погоды для передачи в шаблон."""

    current_time = datetime.now()
    time_3_days = current_time + timedelta(days=3)
    data = []

    for time, temp, wind_speed, precipitation in zip(
        weather["hourly"]["time"],
        weather["hourly"]["temperature_2m"],
        weather["hourly"]["wind_speed_10m"],
        weather["hourly"]["precipitation"]
    ):
        time_dt = datetime.fromisoformat(time)
        if 0 <= (
            time_dt - current_time
        ).total_seconds() <= TOTAL_SECONDS_IN_3_DAYS:
            data.append({
                "time": time_dt,
                "temp": temp,
                "wind_speed": wind_speed,
                "precipitation": precipitation
            })

    return {
        "current_time": current_time,
        "time_3_days": time_3_days,
        "data": data
    }


def index(request):
    if request.POST:
        form = forms.WeatherForm(request.POST)
        if form.is_valid():
            try:
                city = form.cleaned_data["city"]
                latitude, longitude, timezone = get_city_coordinates(city)
                weather = get_weather(latitude, longitude, timezone)
                formatted_weather = get_formatted_weather(weather)
                context = {
                    "city": city,
                    "weather": formatted_weather["data"],
                    "units": weather["hourly_units"],
                    "days": {"current_time": formatted_weather["current_time"],
                             "time_3_days": formatted_weather["time_3_days"]}
                }
                return render(request, "weather/weather.html", context)
            except (ValueError, requests.RequestException) as err:
                context = {"message": str(err)}
                return render(request, "weather/error_message.html", context)
    form = forms.WeatherForm()
    context = {"form": form}
    return render(request, "weather/index.html", context)
