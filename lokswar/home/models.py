from django.db import models


class TopNews(models.Model):
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










