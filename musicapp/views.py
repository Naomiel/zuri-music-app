from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<center><h1>Hello You are welcome</h1><h2><br /> To </h2><br><h2> Naomi Zuri Music App <br/> Enjoy Music on  the go!</h2></center>")