from django.contrib import admin

from .models import RequestM


@admin.register(RequestM)
class RequestMAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'info', 'created_at', 'updated_at')
    readonly_fields = ('name', 'phone', 'info', 'created_at', 'updated_at')
