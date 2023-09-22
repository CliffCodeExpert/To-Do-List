from django.contrib import admin
from .models import List,Profile

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created_at','completed')
    list_filter = ('user', 'created_at')

admin.site.register(Profile)