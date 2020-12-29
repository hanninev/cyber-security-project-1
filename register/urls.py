from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name='index'),
    path('add/', views.reqisterAction, name='register'),
    path('modify/<int:memberid>', views.editView, name='modify'),
    path('modify/edit/', views.editAction, name='edit'),
    path('login/edit/', views.editAction, name='edit'),
    path('login/', views.loginAction, name='login'),

]