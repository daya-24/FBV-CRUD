from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginview, name='login1'),
    path('register/', views.registerView, name='register1'),
    path('logout/', views.logoutView, name='logout1')
]