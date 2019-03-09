from django.shortcuts import render,get_object_or_404
from .models import TopNews,RecentNews,PopluarPostNews,VideoNews
from django.views.generic import ListView,DetailView
from django.utils import timezone
from django.http import HttpResponse, Http404



def top_news_list(request):
    queryset = list(TopNews.objects.all())
    queryset0 = list(RecentNews.objects.all())
    queryset1 = list(PopluarPostNews.objects.all())
    queryset2 = list(VideoNews.objects.all())

   
    context = {
        'queryset':queryset,
        'queryset0':queryset0,
        'queryset1':queryset1,
        'queryset2':queryset2,

    }

    return render(request, "home_list.html",context)

    

# class TopNewsDetail(DetailView):
    
#     template_name = 'top_detail.html'
#     def get_object(self):

#         return get_object_or_404(TopNews, slug=self.kwargs.get('slug', None))


def top_news_detail(request, slug):
    detail = get_object_or_404(TopNews, slug=slug)

   


    context = {
        'detail':detail,
        
 }
    return render(request,'top_detail.html',context)

def recent_news_detail(request, slug):
    detail0 = get_object_or_404(RecentNews, slug=slug)


    context = {
        'detail0':detail0,

    }
    return render(request,'top_detail.html', context)


def popular_news_detail(request,slug):
    detail1 = get_object_or_404(PopluarPostNews, slug=slug)

    context = {
        'detail1':detail1,
    }

    return render(request,'top_detail.html', context)
