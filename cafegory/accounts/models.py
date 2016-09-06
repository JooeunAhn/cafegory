from django.db import models
from django.conf import settings
# Create your models here.

class Comment_to_us(models.Model):
    message = models.TextField(max_length=1000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True)