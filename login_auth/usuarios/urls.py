from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path ('cadastro/', views.cadastro, name='cadastro'),
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('plataforma/', views.plataforma, name='plataforma')

]