# -*- coding: utf-8 -*-
from django.db import models


class person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=50)

    def __unicode__(self):
        return self.name


# class user(models.Model):
#     name = models.CharField(max_length=50)
#     pwd = models.CharField(max_length=50)
#     age = models.IntegerField(default=50)
#     email = models.CharField(max_length=50)
#
#     def __unicode__(self):
#         return self.name


class image(models.Model):
    photo = models.ImageField(upload_to='photos', default='user1.jpg')
    name = models.CharField(max_length=50)
    image_owner = models.CharField(max_length=50, default="")

    def __unicode__(self):
        return self.name


class blog(models.Model):
    blog_time = models.DateTimeField(auto_now=True)
    blog_name = models.CharField(max_length=50)
    blog_context = models.CharField(max_length=1000)
    author = models.CharField(max_length=50)


class Comment(models.Model):
    blog = models.ForeignKey(blog)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField(max_length=1000)
    crete_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
