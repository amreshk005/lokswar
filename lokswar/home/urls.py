
from django.urls import path,include
from . import views


urlpatterns = [
    # path('',views.HomeListView.as_view(),name='home'),
    path('',views.top_news_list,name='home'),
    path('(<slug>[\w-]+)/',views.product_detail_view,name='home_detail')

    
]
