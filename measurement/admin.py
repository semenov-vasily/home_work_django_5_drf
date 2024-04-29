from django.contrib import admin
from django.utils.safestring import mark_safe

from measurement.models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    list_editable = ('description',)
    ordering = ['id']
    fields = ['name', 'description']
    save_on_top = True
    list_per_page = 10


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'sensor', 'temperature', 'created_at', 'post_photo')
    list_display_links = ('id', 'sensor')
    list_editable = ('temperature',)
    ordering = ['id']
    fields = ['sensor', 'temperature', 'post_photo', 'image']
    readonly_fields = ['post_photo']
    save_on_top = True
    list_per_page = 10

    @admin.display(description="Изображение")
    def post_photo(self, measurement: Measurement):
        if measurement.image:
            return mark_safe(f"<img src='{measurement.image.url}' width=50>")
        return "Без фото"
