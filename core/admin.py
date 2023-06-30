from django.contrib import admin

from core.models import Sneaker


@admin.register(Sneaker)
class SneakerAdmin(admin.ModelAdmin):
    pass
