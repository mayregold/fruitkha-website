from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'fruitkhaApp/index.html')

def base(request):
    return render(request, 'fruitkhaApp/base.html')

def index_2(request):
    return render(request, 'fruitkhaApp/index_2.html')

def about(request):
    return render(request, 'fruitkhaApp/about.html')

def cart(request):
    return render(request, 'fruitkhaApp/cart.html')

def checkout(request):
    return render(request, 'fruitkhaApp/checkout.html')

def contact(request):
    return render(request, 'fruitkhaApp/contact.html')

def news(request):
    return render(request, 'fruitkhaApp/news.html')

def shop(request):
    return render(request, 'fruitkhaApp/shop.html')

def singlenews(request):
    return render(request, 'fruitkhaApp/single-news.html')

def singleproduct(request):
    return render(request, 'fruitkhaApp/single-product.html')
