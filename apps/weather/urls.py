from django.urls import path

from apps.weather import views


app_name = "apps.weather"

urlpatterns = [
    # path("", views.GetCityView.as_view(), name="index"),
    path("", views.index, name="index")
]
