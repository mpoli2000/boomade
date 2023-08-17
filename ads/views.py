from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ads/index.html')

def blog(request):
    return render(request, 'ads/blog.html')

def blog_details(request):
    return render(request, 'ads/blog-details.html')

def services_details(request):
    return render(request, 'ads/services-details.html')

def portfolio_details(request):
    return render(request, 'ads/portfolio-details.html')