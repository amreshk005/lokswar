
from django.urls import path,include,re_path
from . import views

app_name='home'

urlpatterns = [
    path('',views.top_news_list,name='list'),
    path('news/',views.news_list,name='news'),
    path('politics/',views.politics_list,name='politics'),
    path('sports/',views.sports_list,name='sports'),
    path('movie/',views.movie_list,name='movie'),
    path('business/',views.business_list,name='business'),
    path('election/',views.election_list,name='election'),
    path('country/',views.country_list,name='country'),
    path('topnews/<slug>/',views.top_news_detail,name='topnews'),
    path('recentnews/<slug>/',views.recent_news_detail,name='recentnews'),
    path('popularnews/<slug>/',views.popular_news_detail,name='popularnews'),
    path('news_detail/<slug>/',views.news_detail,name='news_detail'),
    path('politics_detail/<slug>/',views.politics_detail,name='politics_detail'),
    path('sport_detail/<slug>/',views.sport_detail,name='sport_detail'),
    path('movie_detail/<slug>/',views.movie_detail,name='movie_detail'),
    path('business_detail/<slug>/',views.business_detail,name='business_detail'),
    path('election_detail/<slug>/',views.election_detail,name='election_detail'),
    path('country_detail/<slug>/',views.country_detail,name='country_detail'),
    path('individual_detail/<slug>/',views.individual_detail,name='individual_detail'),

  



    
]
