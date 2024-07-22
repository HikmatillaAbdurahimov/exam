from django.shortcuts import render
from products.views import product_view
from products.models import Categories,Products


def home_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Products.objects.filter(title__icontains=search)
        return render(request, 'shop.html', {'products': products})
    categories = Categories.objects.all()
    products = Products.objects.all()
    context = {
        "categories": categories,
        "products": products,
    }
    return render(request, 'index.html', context)


def product_view(request):
    if request.method=="POST":
        search=request.POST['search']
        products=Products.objects.filter(title__icontains=search)
        return render(request,'shop.html', {'products': products})
    products = Products.objects.all()
    return render(request,'index.html', {'products': products})



def contact_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Products.objects.filter(title__icontains=search)
        return render(request, 'shop.html', {'products': products})
    categories = Categories.objects.all()
    products = Products.objects.all()
    context = {
        "categories": categories,
        "products": products,
    }
    return render(request, 'contact.html', context)

def shop_detail(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Products.objects.filter(title__icontains=search)
        return render(request, 'shop.html', {'products': products})
    categories = Categories.objects.all()
    products = Products.objects.all()
    context = {
        "categories": categories,
        "products": products,
    }
    return render(request,'shop.html',context)


def pages_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Products.objects.filter(title__icontains=search)
        return render(request, 'shop.html', {'products': products})
    categories = Categories.objects.all()
    products = Products.objects.all()
    context = {
        "categories": categories,
        "products": products,
    }
    return render(request, '404.html', context)

def cart_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Products.objects.filter(title__icontains=search)
        return render(request, 'shop.html', {'products': products})
    categories = Categories.objects.all()
    products = Products.objects.all()
    context = {
        "categories": categories,
        "products": products,
    }
    return render(request, 'cart.html', context)

def chackout_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Products.objects.filter(title__icontains=search)
        return render(request, 'shop.html', {'products': products})
    categories = Categories.objects.all()
    products = Products.objects.all()
    context = {
        "categories": categories,
        "products": products,}
    return render(request, 'checkout.html', context)



def testimonial_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Products.objects.filter(title__icontains=search)
        return render(request, 'shop.html', {'products': products})
    categories = Categories.objects.all()
    products = Products.objects.all()
    context = {
        "categories": categories,
        "products": products,
    }
    return render(request, 'testimonial.html', context)

