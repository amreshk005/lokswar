
from django.urls import path,include,re_path
from . import views

app_name='home'

urlpatterns = [
    path('',views.top_news_list,name='list'),
    path('topnews/<slug>/',views.top_news_detail,name='topnews'),
    path('recentnews/<slug>/',views.recent_news_detail,name='recentnews'),
    path('popularnews/<slug>/',views.popular_news_detail,name='popularnews')



    
]
