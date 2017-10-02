from django.http import HttpResponse
from django.core import serializers
from django.contrib import admin
from .models import *
# Register your models here.


def export_as_json(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type="application/json")
    response['Content-Disposition'] = 'attachment; filename={}.json'.format(opts.verbose_name)
    serializers.serialize("json", queryset, stream=response)
    return response
export_as_json.short_description = 'Export to JSON'

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'author', 'created', 'updated']
    list_filter = ['name', 'author', 'created', 'updated']
    actions = [export_as_json]

admin.site.register(Application, ApplicationAdmin)

class LangueAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    actions = [export_as_json]

admin.site.register(Langue, LangueAdmin)

class SectionImageAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    actions = [export_as_json]

admin.site.register(SectionImage, SectionImageAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated', 'typeimage']
    list_filter = ['name', 'created', 'updated', 'typeimage']
    actions = [export_as_json]

admin.site.register(Image, ImageAdmin)
