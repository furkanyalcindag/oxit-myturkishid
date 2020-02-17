"""oxiterp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path('api/(?P<version>(v1|v2))/', include('patient.urls')),
    # path('hasta/', include('patient.urls',  namespace='patient')),
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('', include('accounts.urls')),
    # path('accounts/', include('django.contrib.auth.urls'))
    path('manager/', include('accounts.urls')),
    # path('egitim/', include('education.urls')),
    path('baven/', include('inoks.urls')),
    path('', include('myturkishiid.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
