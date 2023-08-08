from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')
    
def term(request):
    return render(request, 'term.html')

def cosmetic(request):
    return render(request, 'cosmetic.html')

def dryfruits(request):
    return render(request, 'dryfruits.html')

def electronics(request):
    return render(request, 'electronics.html')

def grosary(request):
    return render(request, 'grosary.html')

def kitchen(request):
    return render(request, 'kitchen.html')

def toys(request):
    return render(request, 'toys.html')

def security(request):
    return render(request, 'security.html')


def about(request):
    return render(request, 'about.html')

def payment(request):
    return render(request, 'payment.html')

def shipping(request):
    return render(request, 'shipping.html')

def product(request):
    return render(request, 'product.html')

def demo(request):
    return render(request, 'demo.html')

def cart(request):
    return render(request, 'cart.html')

def wishlist(request):
    return render(request, 'wishlist.html')




