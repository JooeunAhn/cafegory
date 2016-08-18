from django.shortcuts import render
from cafe.models import Cafe

def index(request):
    cafe_list = Cafe.objects.all()
    return render(request,"cafe/index.html",{cafe_list:cafe_list})
