from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('',views.index , name='index'),
    path('signup',views.signup , name='signup'),
    path('signin',views.signin , name='signin'),
    path('signout',views.signout , name='signout'),
    path('record', views.record , name='record'),
    path('doctorhospital', views.doctorhospital , name='doctorhospital'),
    path('heartdetail',views.heartdetail,name='heartdetail'),
    path('feedback/', views.feedback, name='feedback'),
]
