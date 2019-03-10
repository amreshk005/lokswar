from django.contrib import admin

# Register your models here.

from .models import (
    News,
    Movie,
    Sport,
    TopNews,
    Politics,
    Business,
    Election,
    Country,
    VideoNews,
    RecentNews,
    PopluarPostNews,
    Individual,

   

)



@admin.register(TopNews)
class TopNewsAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']
    list_display = ['__str__','slug']

@admin.register(RecentNews)
class RecentNewsAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']
    list_display = ['__str__','slug']

@admin.register(PopluarPostNews)
class PopluarPostNewsAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']
    list_display = ['__str__','slug']

@admin.register(VideoNews)
class VideoNewsAdmin(admin.ModelAdmin):
    fields = ['title','url']
 

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']
    list_display = ['__str__','slug']

@admin.register(Politics)
class PoliticsAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']
    list_display = ['__str__','slug'] 

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']
    list_display = ['__str__','slug']  

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']
    list_display = ['__str__','slug'] 

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']
    list_display = ['__str__','slug'] 

@admin.register(Election)
class BusinessAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']
    list_display = ['__str__','slug'] 

@admin.register(Country)
class BusinessAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']
    list_display = ['__str__','slug']    


@admin.register(Individual)
class BusinessAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']
    list_display = ['__str__','slug']    





