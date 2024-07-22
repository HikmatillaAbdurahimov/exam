from django.shortcuts import render
from .models import Categories,Products



""" bu bizga databaseda malumot olib saytda ko'rinish beradi """
def product_view(request):
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
    return render(request, 'shop.html', context)
