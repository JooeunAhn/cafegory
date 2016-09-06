from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

class Cafe(models.Model):
    name = models.CharField(max_length=100)
    is_24 = models.BooleanField(default=False)
    is_smoke = models.BooleanField(default=False)
    is_wifi = models.BooleanField(default=False)
    is_plug = models.BooleanField(default=False)
    is_parking = models.BooleanField(default=False)
    address = models.CharField(max_length=100)
    latlng = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='cafe_images')
    timeinfo = models.CharField(max_length=100, default="")
    tel = models.CharField(max_length=15)
    CHOICES = (
        ("서울대입구","서울대입구"),
        ("강남역","강남역"),
        ("홍대입구","홍대입구"),
        ("한양대","한양대"),
        )
    location = models.CharField(max_length=20, choices = CHOICES, default="서울대입구")
    end_time = models.CharField(max_length=40, default="")
    ratings = GenericRelation(Rating, related_query_name='ratings')

    @property
    def lat(self):
        if self.latlng:
            return self.latlng.split(',')[0]
        return None

    @property
    def lng(self):
        if self.latlng:
            return self.latlng.split(',')[1]
        return None

class Cafe_comment(models.Model):
    message = models.TextField(max_length=500)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    cafe = models.ForeignKey(Cafe)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
