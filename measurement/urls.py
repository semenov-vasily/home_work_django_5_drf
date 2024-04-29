from django.contrib import admin
from django.urls import path

from measurement.views import ListSensor, UpdateDeleteSensor, AddMeasurement, SensorInfoView, MeasurementsInfoView

urlpatterns = [
    path('sensors/', ListSensor.as_view()),
    path('sensors/<int:pk>/', UpdateDeleteSensor.as_view()),
    path('measurements/', AddMeasurement.as_view()),
    path('sensors/info/<int:pk>/', SensorInfoView.as_view()),
    path('measurements/info/<int:pk>/', MeasurementsInfoView.as_view()),
]


