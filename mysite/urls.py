"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import settings
from mysite import views as learn_views
from django.conf.urls.static import static
admin.autodiscover()
urlpatterns = [
    url(r'^regist/$', learn_views.regist),  # new
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',learn_views.login),
    url(r'^look/$',learn_views.look),
    url('^update/$',learn_views.update),
    url('^success/$',learn_views.success),
    url('^myphoto/$',learn_views.updateInfo),
    url('^back_in/$',learn_views.back_in),
    url('^write/$',learn_views.write),
    url('^write_blog/$',learn_views.write_blog),
    url('^look/update_infor/', learn_views.update_information)
    # url(r'^ckeditor/', include('ckeditor.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
