from django.urls import path
from .views import Test, GetWeatherData, TaskView

urlpatterns = [
    path('', Test.as_view(), name='test'),
    path('weather/', GetWeatherData.as_view(), name='weather'),
    path('task/', TaskView.as_view(), name='task'),
]
