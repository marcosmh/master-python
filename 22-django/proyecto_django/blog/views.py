from django.shortcuts import render
from .models import Category, Article

# Create your views here.

def category(request):

    cat = "Category"
    
    return render(request,"blog/category.html",{
        "cat": cat
    })


def article(request):

    article = "Article"
    
    return render(request,"blog/article.html",{
        "article": article
    })