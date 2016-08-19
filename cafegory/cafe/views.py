from django.shortcuts import render, get_object_or_404, redirect
from cafe.models import Cafe
from cafe.forms import CafeForm

def index(request):
	cafe_list = Cafe.objects.all()
	return render(request,"cafe/index.html",{"cafe_list":cafe_list})

def cafe_detail(request,pk):
	cafe = get_object_or_404(Cafe,pk=pk)
	lat = cafe.lat
	lng = cafe.lng
	return render(request,"cafe/cafe_detail.html",{"cafe":cafe, "lat":lat ,"lng":lng })

def cafe_new(request):
    if request.method == "POST":
        form = CafeForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect("cafe:cafe_detail",form.pk)
    else:
        form = CafeForm()
    return render(request, "cafe/cafe_form.html",{"form":form,})

def cafe_edit(request,pk):
    cafe = Cafe.objects.get(pk=pk)
    if request.method == "POST":
        form = CafeForm(request.POST, request.FILES,instance=cafe)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect("cafe:cafe_detail", form.pk)
    else:
        form = CafeForm(instance=cafe)
    return render(request, "cafe/cafe_form.html",{"form":form,})

