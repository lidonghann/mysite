# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import blog, image, Comment

admin.site.register(blog)
admin.site.register(image)
admin.site.register(Comment)

# Register your models here.
