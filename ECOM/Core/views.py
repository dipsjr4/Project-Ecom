from django.shortcuts import render

from products.models import Category, Item


# Create your views here.
def index(request):
    items = Item.objects.filter()
    categories = Category.objects.all()

    return render(request, 'pages/index.html', {
        'categories': categories,
        'items': items
    })


def contact(request):
    return render(request, 'pages/contact.html')


def about(request):
    return render(request, 'pages/about.html')


def browse(request):
    return render(request, 'pages/browse.html')


def cart(request):
    context = {}
    return render(request, 'pages/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'pages/checkout.html', context)
