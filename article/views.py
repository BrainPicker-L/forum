from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.


def article_list(request):
    context = {}
    if "searchtext" in request.GET:
        articles = Article.objects.filter(title__icontains=request.GET['searchtext'])
        if articles.count() == 0:
            articles = Article.objects.filter(content__icontains=request.GET['searchtext'])
    elif "typename" in request.GET:
        articles = Article.objects.filter(article_type__type_name__contains=request.GET['typename'])

    else:
        articles = Article.objects.all()
    context["article_types"] = ArticleType.objects.all()
    context["articles"] = articles.order_by("-created_time")
    return render(request,'articles-list.html',context)