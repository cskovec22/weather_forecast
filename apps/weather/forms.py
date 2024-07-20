from django import forms


class WeatherForm(forms.Form):
    city = forms.CharField(label="Город", max_length=50)
