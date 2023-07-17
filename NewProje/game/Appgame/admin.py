from django.contrib import admin
from .models import *




@admin.register(Userinfo)
class Userinfo(admin.ModelAdmin):

    list_display = ('user','password')
    list_filter = ('user',)
    search_fields = ('user__username',)

