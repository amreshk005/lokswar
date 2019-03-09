from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import UserManager
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
# 


class TopNews(models.Model):
    title = models.CharField(max_length=120,null=False)
    slug = models.SlugField(blank=True,null=True,unique=True,default=None)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=False,blank=False,default="default.jpg")
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)

    

    def get_absolute_url(self):
        return reverse("home:topnews",kwargs={'slug':self.slug})

    def __str__(self):
        return self.title
        
 
    def __unicode__(self):
        return self.title


class RecentNews(models.Model):
    title = models.CharField(max_length=120,null=False)
    slug = models.SlugField(blank=True,null=True,unique=True,default=None)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=False,blank=False,default="default.jpg")
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)


    def get_absolute_url(self):
        return reverse("home:recentnews",kwargs={'slug':self.slug})


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class PopluarPostNews(models.Model):
    title = models.CharField(max_length=120,null=False)
    slug = models.SlugField(blank=True,null=True,unique=True,default=None)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=False,blank=False,default="default.jpg")
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)
    
    def get_absolute_url(self):
        return reverse("home:popularnews",kwargs={'slug':self.slug})

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



class News(models.Model):
    title = models.CharField(max_length=120,null=False)
    slug = models.SlugField(blank=True,null=True,unique=True,default=None)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=False,blank=False,default="default.jpg")
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)

    

    def get_absolute_url(self):
        return reverse("home:news_detail",kwargs={'slug':self.slug})

    def __str__(self):
        return self.title
        
 
    def __unicode__(self):
        return self.title



class Politics(models.Model):
    title = models.CharField(max_length=120,null=False)
    slug = models.SlugField(blank=True,null=True,unique=True,default=None)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=False,blank=False,default="default.jpg")
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)

    

    def get_absolute_url(self):
        return reverse("home:politics_detail",kwargs={'slug':self.slug})

    def __str__(self):
        return self.title
        
 
    def __unicode__(self):
        return self.title

class Sport(models.Model):
    title = models.CharField(max_length=120,null=False)
    slug = models.SlugField(blank=True,null=True,unique=True,default=None)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=False,blank=False,default="default.jpg")
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)

    

    def get_absolute_url(self):
        return reverse("home:sport_detail",kwargs={'slug':self.slug})

    def __str__(self):
        return self.title
        
 
    def __unicode__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=120,null=False)
    slug = models.SlugField(blank=True,null=True,unique=True,default=None)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=False,blank=False,default="default.jpg")
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)

    

    def get_absolute_url(self):
        return reverse("home:movie_detail",kwargs={'slug':self.slug})

    def __str__(self):
        return self.title
        
 
    def __unicode__(self):
        return self.title

class Business(models.Model):
    title = models.CharField(max_length=120,null=False)
    slug = models.SlugField(blank=True,null=True,unique=True,default=None)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=False,blank=False,default="default.jpg")
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)

    

    def get_absolute_url(self):
        return reverse("home:business_detail",kwargs={'slug':self.slug})

    def __str__(self):
        return self.title


class Election(models.Model):
    title = models.CharField(max_length=120,null=False)
    slug = models.SlugField(blank=True,null=True,unique=True,default=None)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=False,blank=False,default="default.jpg")
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)

    

    def get_absolute_url(self):
        return reverse("home:election_detail",kwargs={'slug':self.slug})

    def __str__(self):
        return self.title
        
 
    def __unicode__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=120,null=False)
    slug = models.SlugField(blank=True,null=True,unique=True,default=None)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=False,blank=False,default="default.jpg")
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)

    

    def get_absolute_url(self):
        return reverse("home:country_detail",kwargs={'slug':self.slug})

    def __str__(self):
        return self.title








