from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('for_siths/', views.for_siths, name='for_siths'),
    path('for_recruits/', views.for_recruits, name='for_recruits'),
    path('for_siths/sith_registration/', views.sith_registration, name='sith_registration'),
    path('for_recruits/recruit_registration/', views.recruit_registration, name='recruit_registration'),
    path('for_recruits/recruit_registration/test_result', views.test_result, name='test_result')
]