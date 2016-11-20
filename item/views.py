from django.shortcuts import render

def item(request,pk):
	c = {}
	c["pk"] = pk
	return(render(request,"item.html"))
