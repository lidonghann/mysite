# coding:utf-8
# from django.http import HttpResponse
from django.shortcuts import render
import learn.models
from learn.models import person
# from learn.models import user
from learn.models import blog
from django.http import HttpResponse
from learn.forms import Addform
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import traceback
from mysite import settings
from learn import models
import time
import os, sys
from learn.models import image
from time import strftime, gmtime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json

@csrf_exempt
def regist(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        pwd = request.POST['pwd']
        email = request.POST['email']
        p = User(username=name, password=pwd, email=email, first_name=age)
        # p.name = a
        # p.age = b
        p.save()
        return render(request, 'login.html')
    else:
        return render(request, 'regist.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        pwd = request.POST['pwd']
        c = User.objects.filter(username=name, password=pwd).first()
        try:
            request.session['id'] = c.id
            if c:
                request.session['username'] = c.username
                username = request.session['username']
                blog_information = blog.objects.filter(author=username)
                return render(request, 'success.html', {'user': c, 'blog': blog_information})
            else:
                return HttpResponse("登陆失败")
        except AttributeError:
            return HttpResponse("登陆失败,请检查用户名密码是否正确")
    else:
        return render(request, 'login.html')
        # models.person.objects.create(name="lidonghan",age=23)
        # p=person(name="lhkh",age=21)
        # p.save()
        # person.objects.get_or_create(name="WZT", age=23)
        # person.objects.all()
        # str=person.objects.filter(name__contains="li").update(name='www')


        # name = request.POST.get('name', '')
        # return render(request, 'base.html',{'str':str})
# @login_required
@csrf_exempt
def look(request):
    print request.GET
    id = request.session['id']
    # pwd=request.GET.get('pwd')
    user_info = User.objects.filter(id=id).first()
    if user_info:
        dictw = {}
        dictw['username'] = user_info.username
        dictw['age'] = user_info.first_name
        dictw['email'] = user_info.email
        dictw['id'] = user_info.id
        return render(request, 'look.html', {'user': dictw})
        # print user, type(user)
        # data_dict = {}
        # for i in user:
        # print i.age
        # data_dict['name'] = i.name
        # data_dict['age'] = i.age
        # print data_dict


@csrf_exempt
def update_information(request):
    if request.method == 'GET':
        id = request.GET['id']
        username = request.GET['name']
        userage = request.GET['age']
        email = request.GET['email']
        new_user = User.objects.filter(id=id).first()
        new_user.username = username
        new_user.first_name = userage
        new_user.email = email
        new_user.save()
        return render(request, 'update_success.html', {'user': new_user})
    else:
        pass


@csrf_exempt
def update(request):
    print ("开始执行update")
    if request.method == 'POST':
        pwd = request.POST['pwd']
        id = request.POST['id']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']
        uu = User.objects.filter(id=id, pwd=pwd).first()
        if uu:
            uu.password = pwd2
            uu.save()
            return render(request, 'update_success.html', {'user': uu})
        else:
            return HttpResponse('密码不正确')
    else:
        user_id = request.GET['id']
        return render(request, 'update.html', {'user_id': user_id})


def success(request):
    id = request.session['id']
    print "444444444", id
    username = request.session['username']
    information = dict()
    information['id'] = id
    information['username'] = username
    blog_information = blog.objects.filter(author=username)
    print blog_information
    for a in blog_information:
        print a, "1111111111111111"
    return render(request, 'success.html', {'user': information, 'blog': blog_information})


@csrf_exempt
# def updateInfo(request):
#     if request.method == 'POST':
#         photo = request.FILES['picfile']
#         if photo:
#             phototime = request.session['name'] + str(time.time()).split('.')[0]
#             photo_last = str(photo).split('.')[-1]
#             photoname = os.path.join('photos', '%s.%s' % (phototime, photo_last))
#             img = Image.open(photo)
#             file_path = os.path.join(settings.STATIC_URL, 'upload')
#             print 'file_path + photoname:', os.path.join(file_path, photoname)
#             img.save(os.path.join(file_path, photoname))
#             im=image(name=phototime,img=file_path)
#             im.save()
#             dict={}
#             dict['name']=phototime
#             dict['road']=file_path + photoname
#             return render(request, 'photo.html', {'dict':dict})
#         return HttpResponse('图片为空')
#     elif request.method == 'GET':
#         return render(request, 'photo.html')
def update_info(request):
    if request.method == 'POST':
        photo = request.FILES['picfile']
        if photo:
            phototime = request.session['username'] + str(time.time()).split('.')[0]
            photo_last = str(photo).split('.')[-1]
            photoname = 'media/photos/%s.%s' % (phototime, photo_last)
            des_origin_f = open(photoname, "ab")
            for chunk in photo.chunks():
                des_origin_f.write(chunk)
            des_origin_f.close()
            image_owner = request.session['username']
            count = models.image.objects.create(photo=photoname, name=phototime, image_owner=image_owner)
            if count:
                # dict={}
                # dict['name']=phototime
                # dict['road']=''.join(['/', photoname])
                dicta = image.objects.filter(image_owner=image_owner)
                photo_inform = []
                for foo in dicta:
                    temp = dict()
                    temp['name'] = foo.name
                    temp['road'] = ''.join(['/', unicode(foo.photo)])
                    photo_inform.append(temp)
                json_photo = json.dumps(photo_inform)
                print json_photo, "444444444444445"
                return render(request, 'index.html', locals())
            else:
                return HttpResponse('上传失败')
        return HttpResponse('图片为空')
    elif request.method == 'GET':
        image_owner = request.session['username']
        photo_inform_all = image.objects.filter(image_owner=image_owner)
        photo_inform = []
        for foo in photo_inform_all:
            temp = dict()
            temp['name'] = foo.name
            temp['road'] = ''.join(['/', unicode(foo.photo)])
            photo_inform.append(temp)
        json_photo = json.dumps(photo_inform)
        print json_photo, "444444444444445"
        return render(request, 'index.html', locals())


def back_in(request):
    id = request.session['id']
    username = request.session['username']
    information = dict()
    information['id'] = id
    information['name'] = username
    blog_information = blog.objects.filter(author=username)
    return render(request, 'success.html', {'user': information, 'blog': blog_information})


def write(request):
    name = request.session['username']
    id = request.session['id']
    information = dict()
    information['id'] = id
    information['name'] = name
    return render(request, 'write.html', {'user': information})


@csrf_exempt
def write_blog(request):
    if request.method == 'POST':
        tit = request.POST['tit']
        con = request.POST['con']
        username = request.session['username']
        this_time = strftime("%Y-%m-%d", gmtime())
        b = blog(blog_time=this_time, blog_name=tit, blog_context=con, author=username)
        b.save()
        # dict={}
        # dict ['author']=b.author
        # dict['time']=b.blog_time
        # dict['context']=b.blog_context
        # dict['title']=b.blog_name
        dicta = blog.objects.filter(author=username)
        # print "type(dicta)", type(dicta)
        # dictb = []
        # for foo in dicta:
        #     temp = dict()
        #     temp['author'] = foo.author
        #     temp['blog_time'] = foo.blog_time
        #     temp['blog_context'] = foo.blog_context
        #     print temp['blog_context'], "temp['blog_context']"
        #     temp['blog_name'] = foo.blog_name
        #     dictb.append(temp)
        #     print dictb
        return render(request, 'success.html', {'blog': dicta})
    else:
        return HttpResponse('提交失败')
