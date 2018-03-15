# coding:utf-8
# from django.http import HttpResponse
from django.shortcuts import render
import learn.models
from learn.models import person
from learn.models import user
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


@csrf_exempt
def regist(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        pwd = request.POST['pwd']
        email = request.POST['email']
        p = user(name=name, pwd=pwd, email=email, age=age)
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
        c = user.objects.filter(name=name, pwd=pwd).first()
        try:
            request.session['name'] = c.name
            request.session['id'] = c.id
            print "idddddddddddddd", request.session['id']
            print "request.session['name']", request.session['name']
            if c:
                return render(request, 'success.html', {'user': c})
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


@csrf_exempt
def look(request):
    print request.GET
    id = request.session['id']
    # pwd=request.GET.get('pwd')
    user_info = user.objects.filter(id=id).first()
    print user_info.name
    if user_info:
        dictw = {}
        dictw['name'] = user_info.name
        dictw['age'] = user_info.age
        dictw['email'] = user_info.email
        dictw['id'] = user_info.id
        print "dictw", dictw
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
        new_user = user.objects.filter(id=id).first()
        new_user.name = username
        new_user.age = userage
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
        uu = user.objects.filter(id=id, pwd=pwd).first()
        if uu:
            uu.pwd = pwd2
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
    name =request.session['name']
    infor = {}
    infor['id'] = id
    infor['name'] = name
    return render(request, 'success.html', {'user': infor})


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
def updateInfo(request):
    if request.method == 'POST':
        photo = request.FILES['picfile']
        if photo:
            phototime = request.session['name'] + str(time.time()).split('.')[0]
            photo_last = str(photo).split('.')[-1]
            photoname = 'media/photos/%s.%s' % (phototime, photo_last)
            des_origin_f = open(photoname, "ab")
            for chunk in photo.chunks():
                des_origin_f.write(chunk)
            des_origin_f.close()
            count = models.image.objects.create(photo=photoname, name=phototime)
            if count:
                # dict={}
                # dict['name']=phototime
                # dict['road']=''.join(['/', photoname])
                dicta = image.objects.all()
                dictb = []
                for foo in dicta:
                    tmp = {}
                    tmp['name'] = foo.name
                    tmp['road'] = ''.join(['/', unicode(foo.photo)])
                    tmp['length'] = dicta.__len__()
                    dictb.append(tmp)
                print "dictb", dictb
                for aa in dictb:
                    print aa
                    # print "22222", aa.road
                    # print "33333", aa.length
                return render(request, 'index.html', {'dictb': dictb})
            else:
                return HttpResponse('上传失败')
        return HttpResponse('图片为空')
    elif request.method == 'GET':
        return render(request, 'index.html')


def back_in(request):
    id = request.session['id']
    print "222222222222", id
    name = request.session['name']
    infor = {}
    infor['id'] = id
    infor['name'] = name
    return render(request, 'success.html', {'user': infor})


def write(request):
    name = request.session['name']
    id = request.session['id']
    infor = {}
    infor['id'] = id
    infor['name'] = name
    return render(request, 'write.html', {'user': infor})


@csrf_exempt
def write_blog(request):
    if request.method == 'POST':
        tit = request.POST['tit']
        con = request.POST['con']
        name = request.session['name']
        this_time = strftime("%Y-%m-%d", gmtime())
        b = blog(blog_time=this_time, blog_name=tit, blog_context=con, author=name)
        b.save()
        # dict={}
        # dict ['author']=b.author
        # dict['time']=b.blog_time
        # dict['context']=b.blog_context
        # dict['title']=b.blog_name
        dicta = blog.objects.filter(author=name)
        dictb = []
        for foo in dicta:
            temp = {}
            temp['author'] = foo.author
            temp['time'] = foo.blog_time
            temp['context'] = foo.blog_context
            temp['title'] = foo.blog_name
            dictb.append(temp)
        return render(request, 'success.html', {'dictb': dictb})
    else:
        return HttpResponse('提交失败')
