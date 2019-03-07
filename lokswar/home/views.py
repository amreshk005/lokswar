from django.shortcuts import render
from .models import TopNews,RecentNews,PopluarPostNews,VideoNews
from django.views.generic import ListView,DetailView
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
#     model = TopNews


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['queryset'] = 


def product_detail_view(request,pk=None,**kwargs):
    querset = Product.objects.all()
    isinstance 








