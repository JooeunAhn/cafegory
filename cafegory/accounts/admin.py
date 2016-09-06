from django.contrib import admin
from .models import Comment_to_us

class Comment_to_us_Admin(admin.ModelAdmin):
    list_display = ['id',"author",'message',]

admin.site.register(Comment_to_us,Comment_to_us_Admin)

# Register your models here.
