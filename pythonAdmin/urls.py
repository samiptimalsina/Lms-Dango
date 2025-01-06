"""
URL configuration for pythonAdmin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from pythonAdmin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('about-us',views.About,name="about"),
    path('teams',views.Team,name="team"),
    path('services',views.Services,name="services"),
    path('why-us',views.WhyUs,name="why"),
    path('home/course/<int:courseId>',views.Course),
    path('contact-us',views.contactUs,name="contact"),

]


