from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_blog, name='home-blog'),
    path('category/<str:category_name>/', views.home_blog, name='category-page'),
    path('tag/<str:tag_name>/', views.home_blog, name='tag-page'),
    path('author/<str:author_username>/', views.home_blog, name='author-page'),
    path('search/', views.blog_search, name='blog-search'),
    path('tag_test/', views.tag_test),
    path('<slug:slug>/', views.single_blog, name='single-blog'),



]