from django.shortcuts import render
from cafe.models import Cafe

def index(request):
	return render(request,"cafe/index.html",{
		})

