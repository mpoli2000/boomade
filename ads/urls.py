from django.urls import path
from . import views

app_name = 'ads'
urlpatterns = [
    path('ads', views.index, name='index'),
    path('ads/blog/', views.blog, name='blog'),
    path('ads/blog_details/', views.blog_details, name='blog-details'),
    path('ads/services_details/', views.services_details, name='services-details'),
    path('ads/portfolio_details/', views.portfolio_details, name='portfolio-details'),
]