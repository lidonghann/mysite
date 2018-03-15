# -*- coding: utf-8 -*-
from django.db import models

class person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=50)

    def __unicode__(self):
        return self.name


class user(models.Model):
    name = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)
    age = models.IntegerField(default=50)
    email = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class image(models.Model):
    photo = models.ImageField(upload_to='photos', default='user1.jpg')
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class blog(models.Model):
    blog_time = models.DateTimeField(auto_now=True)
    blog_name = models.CharField(max_length=50)
    blog_context = models.CharField(max_length=200)
    author = models.CharField(max_length=50)


    # Create your models here.
    # from learn.models import person
    # person.objects.create(name="WeizhongTu", age=24)
    # person.objects.create(name="WeizhongTu", age="30")
