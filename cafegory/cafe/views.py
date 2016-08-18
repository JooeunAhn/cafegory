from django.shortcuts import render, get_object_or_404
from cafe.models import Cafe

def index(request):
	cafe_list = Cafe.objects.all()
	return render(request,"cafe/index.html",{"cafe_list":cafe_list})

def cafe_detail(request,pk):
	cafe = get_object_or_404(Cafe,pk=pk)
	lat = cafe.lat
	lng = cafe.lng
	return render(request,"cafe/cafe_detail.html",{"cafe":cafe, "lat":lat ,"lng":lng })

