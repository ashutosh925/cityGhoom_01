from django.urls import path
from newapp import views

urlpatterns = [
    path('', views.index, name='newapp'), 
    path('base', views.base, name = 'base'),
    path('term', views.term, name = 'term'),
    path('cosmetic', views.cosmetic, name = 'cosmetic'),
    path('dryfruits', views.dryfruits, name = 'dryfruits'),
    path('electronics', views.electronics, name = 'electronics'),
    path('grosary', views.grosary, name = 'grosary'),
    path('kitchen', views.kitchen, name = 'kitchen'),
    path('toys', views.toys, name = 'toys'),
    path('security', views.security, name = 'security'),
    path('about', views.about, name = 'about'),
    path('payment', views.payment, name = 'payment'),
    path('shipping', views.shipping, name = 'shipping'),
    path('product', views.product, name = 'product'),
    path('demo', views.demo, name = 'demo'),
    path('cart', views.cart, name = 'cart'),
    path('wishlist', views.wishlist, name = 'wishlist'),
]
