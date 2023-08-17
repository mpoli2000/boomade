from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'append/index.html')

def blog(request):
    return render(request, 'append/blog.html')

def blog_details(request):
    return render(request, 'append/blog-details.html')

def services_details(request):
    return render(request, 'append/services-details.html')

def portfolio_details(request):
    return render(request, 'append/portfolio-details.html')