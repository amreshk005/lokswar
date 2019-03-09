from django.contrib import admin

# Register your models here.

from .models import TopNews,RecentNews,PopluarPostNews,VideoNews



class TopNewsAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']
    
class RecentNewsAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']

class PopluarPostNewsAdmin(admin.ModelAdmin):
    fields = ['title','slug','description','image','author','date','featured']

class VideoNewsAdmin(admin.ModelAdmin):
    fields = ['title','url']



admin.site.register(TopNews,TopNewsAdmin)
admin.site.register(RecentNews,RecentNewsAdmin)
admin.site.register(PopluarPostNews,PopluarPostNewsAdmin)
admin.site.register(VideoNews,VideoNewsAdmin)


