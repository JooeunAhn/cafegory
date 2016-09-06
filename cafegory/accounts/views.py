from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def mypage(request):
    return render(request,"accounts/mypage.html")