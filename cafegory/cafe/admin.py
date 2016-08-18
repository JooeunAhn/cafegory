from django.contrib import admin
from cafe.models import Cafe
from cafe.forms import CafeForm
# Register your models here.

@admin.register(Cafe)
class PostAdmin(admin.ModelAdmin):
    form = CafeForm
    list_display = ['id', 'name']
    list_display_links = ['name']