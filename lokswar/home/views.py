from django.shortcuts import render
from .models import TopNews,RecentNews,PopluarPostNews,VideoNews
from django.views.generic import ListView,DeleteView
from django.utils import timezone

# class HomeListView(ListView):
#     queryset = TopNews.objects.all()
#     queryset0 = RecentNews.objects.all()
#     queryset1 = PopluarPostNews.objects.all()
#     queryset2 = VideoNews.objects.all()
    
    
#     template_name = 'home_list.html'
#     def get_context_data(self,*args, **kwargs):
#         context = super(HomeListView, self).get_context_data(*args,**kwargs)
#         context['queryset']=self.queryset
#         context['queryset0']=self.queryset0
#         context['queryset1']=self.queryset1
#         context['queryset2']=self.queryset2
        


#         return context


def top_news_list(request):
    queryset = list(TopNews.objects.all())


    context = {
        'queryset':queryset
    }

    return render(request, "home_list.html",context)

