from django.shortcuts import render, get_object_or_404
from .models import Category, Article

# Create your views here.

def list(request):

    articles = Article.objects.all();
    
    return render(request,"articles/list.html",{
        "title": "Artículos",
        "articles": articles
    })


def category(request,category_id):

    #category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category,id=category_id)
    articles = Article.objects.filter(categories=category_id)
    
    
    return render(request,"categories/category.html",{
        "title": "Categorías",
        "category": category,
        "articles": articles
    })

def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request,"articles/detail.html",{
        "article": article
    })

