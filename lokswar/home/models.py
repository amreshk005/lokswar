from django.db import models
from django.urls import reverse
from django.db.models.singnals import pre_save, post_save
from .utils import unique_slug_generator



class TopNews(models.Model):
    title = models.CharField(max_length=120,null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=True,blank=True)
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)


    def get_absolute_url(self):
        return reverse("home:home_detail",kwargs={"slug":self.slug})
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


def top_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(top_pre_save_receiver, sender=TopNews)

class RecentNews(models.Model):
    title = models.CharField(max_length=120,null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=True,blank=True)
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class PopluarPostNews(models.Model):
    title = models.CharField(max_length=120,null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=True,blank=True)
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

class VideoNews(models.Model):
    title = models.CharField(max_length=120, null=False)
    url = models.URLField(null=False,default=None)

    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title










