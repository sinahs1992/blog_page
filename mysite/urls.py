from django.urls import path
from mysite import views

app_name = 'mysite'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('subscribe/', views.subscibe, name='subscibe'),
    path('test2/', views.test2, name='test2'),

]
