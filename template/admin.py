from django.contrib import admin

from template.models import Color


class ColorAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'


admin.site.register(Color, ColorAdmin)
