from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def name(request):
    return render(request, "name.html")

def tom(request):
    return render(request, "tom.html")
