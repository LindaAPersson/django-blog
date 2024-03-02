from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class Aboutadmin(SummernoteModelAdmin):

    list_display = ['title']
    search_fields = ['title']
    summernote_fields = ('content',)

# Register your models here.
