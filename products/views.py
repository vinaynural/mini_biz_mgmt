from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def product_list(request):
    query = request.GET.get('q', '')
    products_list = Product.objects.all()
    
    if query:
        products_list = products_list.filter(
            Q(name__icontains=query)
        )

    paginator = Paginator(products_list, 10) # 10 items per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    return render(request, 'products/product_list.html', {'products': products, 'query': query})

@login_required
def product_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        
        Product.objects.create(name=name, price=price, stock=stock)
        return redirect('product_list')
    
    return render(request, 'products/product_form.html', {'action': 'Add'})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        product.save()
        return redirect('product_list')
    
    return render(request, 'products/product_form.html', {'product': product, 'action': 'Edit'})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})
