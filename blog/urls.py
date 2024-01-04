from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_blog, name='home-blog'),
    # path('test/', views.test, name='test'),
    path('<slug:slug>/', views.single_blog, name='single-blog'),


]