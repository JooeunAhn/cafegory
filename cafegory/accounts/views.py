from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count,Max
from .forms import Comment_to_us_Form
from cafe.models import Cafe, Cafe_comment
from star_ratings.models import UserRating


# Create your views here.

@login_required
def mypage(request):
    if request.method =="POST":
        form = Comment_to_us_Form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.user.is_authenticated:
                form.author = request.user
            form.save()
            messages.success(request,"성공적으로 고객님의 의견이 저장되었습니다. 감사합니다.")
    cafe_comment_list = Cafe_comment.objects.filter(author=request.user).order_by("-updated_at")
    rating_cafe_list = Cafe.objects.filter(ratings__user_ratings__user=request.user).order_by('-ratings__average')
    return render(request,"accounts/mypage.html",{
        "cafe_comment_list":cafe_comment_list,
        "rating_cafe_list":rating_cafe_list,
        })
