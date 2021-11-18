from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('' , views.index , name='index.html'),
    path('drone.html/<int:pk>/', views.drone_detail , name='drone.html'),
    path('about.html', views.about, name='about.html'),
    path('shop.html/<int:pk>/', views.shop, name='shop.html'),
    path('rss.html', views.read_feeds, name='rss.html'),
    path('contact.html' , views.contact ,name= 'contact.html'),
    path('cart.html' ,views.cart , name= 'cart.html'),
    path('register.html' , views.register , name= 'register.html'),
    path('login.html', views.log_in , name = 'login.html'),
    path('checkout.html' , views.checkout , name = 'checkout.html'),
   
   
    path('blog.html', views.blog, name='blog.html'),
    path('drones.html', views.read_drones, name='drones.html'),
    path('logout.html', views.log_out, name='logout.html'),
    path('price_filter.html' , views.filter_by_prices, name='price_filter.html'),

    path(r'^orders/create/login.html' ,views.log_in,name='login.html')
]   
