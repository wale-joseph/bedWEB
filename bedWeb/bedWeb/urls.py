"""bedWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from bedApp import views
from django.conf.urls import url
from cmesbahf.views import x_y_editor

urlpatterns = [
    url(r'^$', views.oneFile, name='oneFile'),
    url(r'^oneFile/', views.oneFile, name='oneFile'),
    path('admin/', admin.site.urls),
    url(r'^twoFiles/', views.twoFiles, name='twoFiles'),
    url(r'^x_y_editor', x_y_editor, name='x_y_editor')
]
