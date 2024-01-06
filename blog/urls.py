from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_blog, name='home-blog'),
    path('category/<str:category_name>/', views.home_blog, name='category-page'),
    path('tag_test/', views.tag_test),
    path('<slug:slug>/', views.single_blog, name='single-blog'),



]