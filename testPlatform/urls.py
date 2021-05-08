"""zeyanTestPlatform URL Configuration

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
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^testplane/',views.TestPlaneView.as_view()),
    url(r'^test_plane_detail/(?P<pk>\d+)',views.test_plane_detail),
    path('testplaneinfo/',views.TestPlaneInfoView.as_view()),
    path('testcase/',views.TestCaseView.as_view()),
]
