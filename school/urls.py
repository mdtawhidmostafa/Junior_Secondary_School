"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('class/',views.clas,name='class'),
    path('login/',views.login,name='login'),
    path('registration/',views.reg,name='reg'),
    path('Contact/',views.cont,name='Contact'),
    path('home/',views.Ahome,name='Ahome'),
    path('out/',views.Logout,name='out'),
    path('abouts/',views.Aabout,name='Aabout'),
    path('classes/',views.Aclas,name='Aclass'),
    path('Contacts/',views.Acont,name='AContact'),
    path('profile/',views.pro,name='profile'),
    path('classes/class4/',views.class4,name='c4'),
    path('classes/class4/math/',views.math4,name='math4'),
    path('classes/class4/math/chapter_1/',views.m4ch1,name='m4ch1'),
    path('classes/class4/math/chapter_2/',views.m4ch2,name='m4ch2'),
    path('classes/class4/math/chapter_3/',views.m4ch3,name='m4ch3'),
    path('classes/class4/math/chapter_4/',views.m4ch4,name='m4ch4'),
    path('classes/class4/math/chapter_5/',views.m4ch5,name='m4ch5'),
    path('classes/class4/math/chapter_6/',views.m4ch6,name='m4ch6'),
    path('classes/class4/math/chapter_7/',views.m4ch7,name='m4ch7'),
    path('classes/class4/math/chapter_8/',views.m4ch8,name='m4ch8'),
    path('classes/class4/math/chapter_9/',views.m4ch9,name='m4ch9'),
    path('classes/class4/math/chapter_10/',views.m4ch10,name='m4ch10'),
    path('classes/class4/math/chapter_11/',views.m4ch11,name='m4ch11'),
    path('classes/class4/math/chapter_12/',views.m4ch12,name='m4ch12'),
    path('classes/class4/math/chapter_13/',views.m4ch13,name='m4ch13'),

    path('classes/class4/Bangla/',views.bangla4,name='bangla4'),
    path('classes/class4/Bangla/chapter_1/',views.b4ch1,name='b4ch1'),
    path('classes/class4/Bangla/chapter_2/',views.b4ch2,name='b4ch2'),
    path('classes/class4/Bangla/chapter_3/',views.b4ch3,name='b4ch3'),
    path('classes/class4/Bangla/chapter_4/',views.b4ch4,name='b4ch4'),
    path('classes/class4/Bangla/chapter_5/',views.b4ch5,name='b4ch5'),
    path('classes/class4/Bangla/chapter_6/',views.b4ch6,name='b4ch6'),
    path('classes/class4/Bangla/chapter_7/',views.b4ch7,name='b4ch7'),
    path('classes/class4/Bangla/chapter_8/',views.b4ch8,name='b4ch8'),
    path('classes/class4/Bangla/chapter_9/',views.b4ch9,name='b4ch9'),
    path('classes/class4/Bangla/chapter_10/',views.b4ch10,name='b4ch10'),
    path('classes/class4/Bangla/chapter_11/',views.b4ch11,name='b4ch11'),
    path('classes/class4/Bangla/chapter_12/',views.b4ch12,name='b4ch12'),
    path('classes/class4/Bangla/chapter_13/',views.b4ch13,name='b4ch13'),
    path('classes/class4/Bangla/chapter_14/',views.b4ch14,name='b4ch14'),
    path('classes/class4/Bangla/chapter_15/',views.b4ch15,name='b4ch15'),
    path('classes/class4/Bangla/chapter_16/',views.b4ch16,name='b4ch16'),
    path('classes/class4/Bangla/chapter_17/',views.b4ch17,name='b4ch17'),
    path('classes/class4/Bangla/chapter_18/',views.b4ch18,name='b4ch18'),
    path('classes/class4/Bangla/chapter_19/',views.b4ch19,name='b4ch19'),

    path('classes/class4/English/',views.english4,name='english4'),
    path('classes/class4/English/chapter_1/',views.e4ch1,name='e4ch1'),
    path('classes/class4/English/chapter_2/',views.e4ch2,name='e4ch2'),
    path('classes/class4/English/chapter_3/',views.e4ch3,name='e4ch3'),
    path('classes/class4/English/chapter_4/',views.e4ch4,name='e4ch4'),
    path('classes/class4/English/chapter_5/',views.e4ch5,name='e4ch5'),
    path('classes/class4/English/chapter_6/',views.e4ch6,name='e4ch6'),
    path('classes/class4/English/chapter_7/',views.e4ch7,name='e4ch7'),
    path('classes/class4/English/chapter_8/',views.e4ch8,name='e4ch8'),
    path('classes/class4/English/chapter_9/',views.e4ch9,name='e4ch9'),

    path('classes/class4/Science/',views.science4,name='science4'),
    path('classes/class4/Science/chapter_1/',views.s4ch1,name='s4ch1'),
    path('classes/class4/Science/chapter_2/',views.s4ch2,name='s4ch2'),
    path('classes/class4/Science/chapter_3/',views.s4ch3,name='s4ch3'),
    path('classes/class4/Science/chapter_4/',views.s4ch4,name='s4ch4'),
    path('classes/class4/Science/chapter_5/',views.s4ch5,name='s4ch5'),
    path('classes/class4/Science/chapter_6/',views.s4ch6,name='s4ch6'),

    path('classes/class4/Religion/',views.religion4,name='religion4'),
    path('classes/class4/Religion/chapter_1/',views.r4ch1,name='r4ch1'),
    path('classes/class4/Religion/chapter_2/',views.r4ch2,name='r4ch2'),
    path('classes/class4/Religion/chapter_3/',views.r4ch3,name='r4ch3'),
    path('classes/class4/Religion/chapter_4/',views.r4ch4,name='r4ch4'),
    path('classes/class4/Religion/chapter_5/',views.r4ch5,name='r4ch5'),

    path('classes/class5/',views.class5,name='c5'),
    path('classes/class6/',views.class6,name='c6'),
    path('classes/class7/',views.class7,name='c7'),
    path('classes/class8/',views.class8,name='c8'),
    




    path('demo/',views.demo,name='demo')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)