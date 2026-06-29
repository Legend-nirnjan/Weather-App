from django.urls import path,include
from .views import get_weather
urlpatterns = [
    path("",get_weather,name='get_weather')
]