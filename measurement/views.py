from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, \
    RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementDataSerializer


# Получение списка всех датчиков и создание нового датчика
class ListSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Обновление и удаление датчика
class UpdateDeleteSensor(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Запись показаний датчика
class AddMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementDataSerializer


# Получение всей информации по датчику с показаниями
class SensorInfoView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# Альтернативное получение всей информации по датчику с показаниями
# class SensorInfoView(RetrieveUpdateAPIView):
# class SensorInfoView(APIView):
#     def get(self, request, pk):
#         sensor = Sensor.objects.filter(id=pk)
#         data = SensorDetailSerializer(sensor, many=True).data
#         return Response(data)


# Получение показаний датчика
class MeasurementsInfoView(APIView):
    def get(self, request, pk):
        measurement = Measurement.objects.filter(sensor_id=pk)
        data = MeasurementDataSerializer(measurement, many=True).data
        return Response(data)
