from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Cafe, Cafe_comment
from .forms import CafeForm, Cafe_comment_Form

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
            if request.user.is_authenticated:
                form.author = request.user
            form.save()
            messages.success(request,"성공적으로 고객님의 의견이 저장되었습니다. 감사합니다.")
    return render(request,"cafe/cafe_list.html",{"cafe_list":cafe_list,"location":location,})


def cafe_detail(request,pk):
    cafe = get_object_or_404(Cafe,pk=pk)
    lat = cafe.lat
    lng = cafe.lng
    comments = Cafe_comment.objects.filter(cafe=cafe).order_by("created_at")

    ##의견듣는곳
    if request.method == "POST" and not request.is_ajax():
        form = Comment_to_us_Form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.user.is_authenticated:
                form.author = request.user
            form.save()
            messages.success(request,"성공적으로 고객님의 의견이 저장되었습니다. 감사합니다.")
    #댓글
    if request.method == "POST" and request.is_ajax() and request.user.is_authenticated:
        form = Cafe_comment_Form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.cafe = cafe
            comment.save()
        return render(request, "cafe/comment_form.html", {
            "cafe": cafe,
            "comments": comments,
            "lat":lat,
            "lng":lng,
        })

    return render(request,"cafe/cafe_detail.html",{"cafe":cafe,"lat": lat,"lng":lng,"comments": comments,})


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


@login_required
def cafe_comment_edit(request, pk):
    if request.method == 'POST':
        comment = get_object_or_404(Cafe_comment, pk=pk)
        if comment.author == request.user:
            cafe = Cafe.objects.get(pk=comment.cafe.pk)
            comment_form = Cafe_comment_Form(request.POST, instance=comment)
            if comment_form.is_valid():
                comment_form.save()
            comments = Cafe_comment.objects.filter(cafe=cafe)
            return render(request, "cafe/comment_form.html", {
                "cafe" : cafe,
                "comments": comments,
            })
    raise Http404


@login_required
def cafe_comment_del(request, pk):
    if request.method == 'POST':
        comment = get_object_or_404(Cafe_comment, pk=pk)
        if comment.author == request.user:
            cafe = Cafe.objects.get(pk=comment.cafe.pk)
            comment.delete()
            # 지연평가를 이용하여 삭제 후 gallery를 가져와서 오류없이 수행
            comments = Cafe_comment.objects.filter(cafe=cafe)
            return render(request, "cafe/comment_form.html", {
                "cafe": cafe,
                "comments": comments,
            })
    raise Http404


