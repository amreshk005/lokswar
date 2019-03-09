from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger,Page

from .models import (
    News,
    Movie,
    Sport,
    Election,
    Country,
    TopNews,
    Politics,
    VideoNews,
    RecentNews,
    Business,
    PopluarPostNews,
)
    
    


# list views start

# home page view
def top_news_list(request):
    queryset = list(TopNews.objects.all())
    queryset0 = list(RecentNews.objects.all())
    queryset1 = list(PopluarPostNews.objects.all())
    queryset2 = list(VideoNews.objects.all())
    queryset3 = list(News.objects.filter().order_by('-id'))[:1]
    queryset4 = list(Politics.objects.filter().order_by('-id'))[:1]
    queryset5 = list(Movie.objects.filter().order_by('-id'))[:1]
    queryset6 = list(Sport.objects.filter().order_by('-id'))[:1]
    queryset7 = list(Election.objects.filter().order_by('-id'))[:1]
    queryset8 = list(Business.objects.filter().order_by('-id'))[:1]


   
    context = {
        'queryset':queryset,
        'queryset0':queryset0,
        'queryset1':queryset1,
        'queryset2':queryset2,
        'queryset3':queryset3,
        'queryset4':queryset4,
        'queryset5':queryset5,
        'queryset6':queryset6,
        'queryset7':queryset7,
        'queryset8':queryset8,


    }

    return render(request, "home_list.html",context)



def news_list(request):
    news = list(News.objects.all())
    page = request.GET.get('page',1)

    paginator = Paginator(news, 2)

    try:
        news_list = paginator.page(page)
    
    except PageNotAnInteger:

        news_list = paginator.page(1)
    
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)

    context = {
        'news_list':news_list,
    }
    return render(request, "category_list/news_category_list.html", context)



def politics_list(request):
    news = list(Politics.objects.all())
    page = request.GET.get('page',1)

    paginator = Paginator(news, 2)

    try:
        news_list = paginator.page(page)
    
    except PageNotAnInteger:

        news_list = paginator.page(1)
    
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)

    context = {
        'news_list':news_list,
    }
    return render(request, "category_list/news_category_list.html", context)

def sports_list(request):
    news = list(Sport.objects.all())
    page = request.GET.get('page',1)

    paginator = Paginator(news, 2)

    try:
        news_list = paginator.page(page)
    
    except PageNotAnInteger:

        news_list = paginator.page(1)
    
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)

    context = {
        'news_list':news_list,
    }
    return render(request, "category_list/news_category_list.html", context)

def movie_list(request):
    news = list(Movie.objects.all())
    page = request.GET.get('page',1)

    paginator = Paginator(news, 2)

    try:
        news_list = paginator.page(page)
    
    except PageNotAnInteger:

        news_list = paginator.page(1)
    
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)

    context = {
        'news_list':news_list,
    }
    return render(request, "category_list/news_category_list.html", context)

def business_list(request):
    news = list(Business.objects.all())
    page = request.GET.get('page',1)

    paginator = Paginator(news, 2)

    try:
        news_list = paginator.page(page)
    
    except PageNotAnInteger:

        news_list = paginator.page(1)
    
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)

    context = {
        'news_list':news_list,
    }
    return render(request, "category_list/news_category_list.html", context)

def election_list(request):
    news = list(Election.objects.all())
    page = request.GET.get('page',1)

    paginator = Paginator(news, 2)

    try:
        news_list = paginator.page(page)
    
    except PageNotAnInteger:

        news_list = paginator.page(1)
    
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)

    context = {
        'news_list':news_list,
    }
    return render(request, "category_list/news_category_list.html", context)



def country_list(request):
    news = list(Country.objects.all())
    page = request.GET.get('page',1)

    paginator = Paginator(news, 2)

    try:
        news_list = paginator.page(page)
    
    except PageNotAnInteger:

        news_list = paginator.page(1)
    
    except EmptyPage:
        news_list = paginator.page(paginator.num_pages)

    context = {
        'news_list':news_list,
    }
    return render(request, "category_list/news_category_list.html", context)
# list view end

# detail view start


def top_news_detail(request, slug):
    detail = get_object_or_404(TopNews, slug=slug)
    

    context = {
            'detail':detail,
            
    }
    return render(request,'home/top_detail.html',context)

def recent_news_detail(request, slug):
    detail0 = get_object_or_404(RecentNews, slug=slug)


    context = {
        'detail0':detail0,

    }
    return render(request,'home/recent_detail.html', context)


def popular_news_detail(request,slug):
    detail1 = get_object_or_404(PopluarPostNews, slug=slug)

    context = {
        'detail1':detail1,
    }

    return render(request,'home/popular_detail.html', context)



def news_detail(request, slug):
    detail2 = get_object_or_404(News, slug=slug)
    
    context = {

        'detail2':detail2,
    }

    return render(request, 'home/news_detail.html', context)


def politics_detail(request, slug):
    detail2 = get_object_or_404(Politics, slug=slug)
    
    context = {

        'detail2':detail2,
    }

    return render(request, 'home/news_detail.html', context)

def sport_detail(request, slug):
    detail2 = get_object_or_404(Sport, slug=slug)
    
    context = {

        'detail2':detail2,
    }

    return render(request, 'home/news_detail.html', context)

def movie_detail(request, slug):
    detail2 = get_object_or_404(News, slug=slug)
    
    context = {

        'detail2':detail2,
    }

    return render(request, 'home/news_detail.html', context)

def business_detail(request, slug):
    detail2 = get_object_or_404(News, slug=slug)
    
    context = {

        'detail2':detail2,
    }

    return render(request, 'home/news_detail.html', context)

def election_detail(request, slug):
    detail2 = get_object_or_404(News, slug=slug)
    
    context = {

        'detail2':detail2,
    }

    return render(request, 'home/news_detail.html', context)

def country_detail(request, slug):
    detail2 = get_object_or_404(News, slug=slug)
    
    context = {

        'detail2':detail2,
    }

    return render(request, 'home/news_detail.html', context)


# detail view end
