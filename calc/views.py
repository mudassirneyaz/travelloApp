from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return  render(request, 'home.html', {'name':"https://www.youtube.com/watch?v=OTmQOjsl0eg&t=5714s"})


def add(request):
	val1 = int(request.POST['num1'])
	val2 = int(request.POST['num2'])
	res = val2+val1

	return render(request, 'result.html', {'result' : res})