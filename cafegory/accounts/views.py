from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Comment_to_us_Form

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

    return render(request,"accounts/mypage.html")