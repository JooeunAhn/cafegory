from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from cafe.models import Cafe
from cafe.forms import CafeForm

from accounts.forms import Comment_to_us_Form


def index(request):
    return render(request, 'cafe/index.html', {})

def cafe_list(request,location):
    converter = {"snu":"서울대입구","hanyang":"한양대"}
    location = converter[location]
    if not Cafe.objects.filter(location=location).exists():
        return redirect("cafe:index")
    cafe_list = Cafe.objects.filter(location=location)

    if request.method == "POST":
        form = Comment_to_us_Form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(request,"성공적으로 고객님의 의견이 저장되었습니다. 감사합니다.")
    return render(request,"cafe/cafe_list.html",{"cafe_list":cafe_list,"location":location,})


def cafe_detail(request,pk):
    if request.method == "POST":
        form = Comment_to_us_Form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(request,"성공적으로 고객님의 의견이 저장되었습니다. 감사합니다.")

    cafe = get_object_or_404(Cafe,pk=pk)
    lat = cafe.lat
    lng = cafe.lng
    return render(request,"cafe/cafe_detail.html",{"cafe":cafe,"lat": lat,"lng":lng,})


@staff_member_required
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


@staff_member_required
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

