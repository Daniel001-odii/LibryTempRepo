from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload'),
    path('logout/', views.logout, name = 'libry'),
    path('signUp/', views.signUp, name = 'signUp'),
    path('reset/', views.reset, name = 'reset'),
    path('profile/', views.profile, name = 'profile'),
]
