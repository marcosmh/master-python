from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'mainapp/index.html',{
        'title': 'inicio'
    })

def about(request):
    return render(request,'mainapp/about.html',{
        'title': 'Acerca de mi'
    })