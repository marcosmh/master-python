from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Category, Article

# Create your views here.

@login_required(login_url="login")
def list(request):

    articles = Article.objects.all();

    #Paginar articulos
    paginator = Paginator(articles,2)
    page = request.GET.get('page')
    page_articles = paginator.get_page(page)
    
    return render(request,"articles/list.html",{
        "title": "Artículos",
        "articles": page_articles
    })

@login_required(login_url="login")
def category(request,category_id):

    #category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category,id=category_id)
    articles = Article.objects.filter(categories=category_id)
    
    
    return render(request,"categories/category.html",{
        "title": "Categorías",
        "category": category,
        "articles": articles
    })

@login_required(login_url="login")
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request,"articles/detail.html",{
        "article": article
    })

