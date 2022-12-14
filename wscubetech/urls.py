"""wscubetech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from wscubetech import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name="home"),
    path('about/',views.aboutUS,name="about"),
    path('services/',views.service,name="service"),
    path('contact/',views.contact,name="contact"),
    path('gallery/',views.gallery,name="gallery"),
    path('fact/',views.fact_us,name="fact"),
    path('page/',views.pageus,name="page"),
    path('userform/',views.userform,name="userform"),
    path('submitform/',views.submitform,name="submitform"),
    path('calculator/',views.calculator),
    path('generic/',views.generic,name="generic"),
    path('elements/',views.elements,name="elements"),
    path('form/',views.employeeforms),

]
