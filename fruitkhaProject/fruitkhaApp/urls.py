from django.urls import path
from . import views
from django.conf.urls import handler404

handler404 = 'fruitkhaApp.views.custom_404'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('index_2/', views.index_2, name='index_2'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('shop/', views.shop, name='shop'),
    path('single-news/', views.singlenews, name='singlenews'),
    path('single-product/', views.singleproduct, name='singleproduct')
]
