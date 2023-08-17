from django.urls import path
from . import views

app_name = 'append'
urlpatterns = [
    path('append', views.index, name='index'),
    path('append/blog/', views.blog, name='blog'),
    path('append/blog_details/', views.blog_details, name='blog-details'),
    path('append/services_details/', views.services_details, name='services-details'),
    path('append/portfolio_details/', views.portfolio_details, name='portfolio-details'),
]