from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Customer
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def customer_list(request):
    query = request.GET.get('q', '')
    customers_list = Customer.objects.all().order_by('-created_at')
    
    if query:
        customers_list = customers_list.filter(
            Q(name__icontains=query) | 
            Q(email__icontains=query) | 
            Q(phone__icontains=query)
        )

    paginator = Paginator(customers_list, 10) # 10 items per page
    page_number = request.GET.get('page')
    customers = paginator.get_page(page_number)
    
    return render(request, 'customers/customer_list.html', {'customers': customers, 'query': query})

@login_required
def customer_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        
        Customer.objects.create(name=name, phone=phone, email=email)
        return redirect('customer_list')
    
    return render(request, 'customers/customer_form.html', {'action': 'Add'})

@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.phone = request.POST.get('phone')
        customer.email = request.POST.get('email')
        customer.save()
        return redirect('customer_list')
    
    return render(request, 'customers/customer_form.html', {'customer': customer, 'action': 'Edit'})

@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customers/customer_confirm_delete.html', {'customer': customer})
