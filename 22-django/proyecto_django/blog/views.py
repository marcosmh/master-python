from django.shortcuts import render
from .models import Category, Article

# Create your views here.

def category(request):

    cat = "Category"
    
    return render(request,"blog/category.html",{
        "cat": cat
    })


def list(request):

    articles = Article.objects.all();
    
    return render(request,"articles/list.html",{
        "title": "Artículos",
        "articles": articles
    })