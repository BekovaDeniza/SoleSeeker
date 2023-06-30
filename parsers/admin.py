from django.contrib import admin
from parsers.models import Site, ParserConfig


@admin.register(Site)
class SneakerAdmin(admin.ModelAdmin):
    pass


@admin.register(ParserConfig)
class SneakerAdmin(admin.ModelAdmin):
    pass
