from django.urls import path
from .import views

urlpatterns = [
   path('', views.index, name='index'),
   path('/register', views.register, name='register'),
   #path('home/',views.home,name='home'),
   path('login/',views.user_login,name='login'),
   path('page/', views.page, name='page'),
]
