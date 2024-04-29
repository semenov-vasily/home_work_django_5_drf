from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название датчика")
    description = models.CharField(max_length=100, verbose_name="Описание датчика")

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name="Measurement", verbose_name="Датчик")
    temperature = models.FloatField(verbose_name="Температура датчика")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время регистрации датчика")
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Фото")

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return f'{self.sensor}'
