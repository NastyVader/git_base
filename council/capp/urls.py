from os import name
from django.urls import path, include
from capp import views

app_name = 'capp'

urlpatterns = [

    path('', views.index, name='index'),
    path('createUnion', views.createUnion, name='createUnion'),
    path('login', views.userLogin, name='userLogin'),
    path('logout', views.userLogout, name='userLogout'),
    path('userInfo', views.userInfo, name='userInfo'),
    path('approve', views.approve, name='approve'),
    path('unionview', views.unionView, name='unionView'),
    path('std', views.students, name='students'),
    path('rules',views.rules, name='rules'),
    path('vote', views.vote, name='vote'),
    path('viewVote', views.viewVote, name='viewVote'),

]