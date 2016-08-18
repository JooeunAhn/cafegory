from django.db import models

class Cafe(models.Model):
    name = models.CharField(max_length=100)
    is_24 = models.BooleanField(default=False)
    is_smoke = models.BooleanField(default=False)
    is_wifi = models.BooleanField(default=False)
    is_plug = models.BooleanField(default=False)
    lnglat = models.CharField(max_length=100)
