from django.shortcuts import render

def user(request):
	return(render(request,"user.html"))

def signup(request):
	return(render(request,"signup.html"))