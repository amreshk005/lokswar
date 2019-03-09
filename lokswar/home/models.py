from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import UserManager
from django.db.models.signals import pre_save,post_save
# 


class TopNews(models.Model):
    title = models.CharField(max_length=120,null=False)
    slug = models.SlugField(blank=True,unique=True,default=None)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=True,blank=True)
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)

    

    def get_absolute_url(self):
        return reverse("home:news",kwargs={'slug':self.slug})

    def __str__(self):
        return self.title
        
 
    def __unicode__(self):
        return self.title


class RecentNews(models.Model):
    title = models.CharField(max_length=120,null=False)
    slug = models.SlugField(blank=True,unique=True,default=None)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=True,blank=True)
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)


    def get_absolute_url(self):
        return reverse("home:news",kwargs={'slug':self.slug})


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class PopluarPostNews(models.Model):
    title = models.CharField(max_length=120,null=False)
    slug = models.SlugField(blank=True,unique=True,default=None)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='lokswar/',null=True,blank=True)
    author = models.CharField(max_length=90,null=False,default=None)
    date = models.DateTimeField(default=None,blank=True)
    featured = models.BooleanField(default=None,null=True)
    
    def get_absolute_url(self):
        return reverse("home:news",kwargs={'slug':self.slug})

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


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = TopNews.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance,new_slug=new_slug)
def pre_save_post_recevier(sender, instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_recevier, sender=TopNews)







