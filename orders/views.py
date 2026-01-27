from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from customers.models import Customer
from products.models import Product
from decimal import Decimal
from django.db import transaction
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.contrib import messages

@login_required
def order_list(request):
    query = request.GET.get('q', '')
    orders_list = Order.objects.all().order_by('-order_date')
    
    if query:
        orders_list = orders_list.filter(
            Q(customer__name__icontains=query) |
            Q(id__icontains=query)
        )

    paginator = Paginator(orders_list, 10)
    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)
    
    return render(request, 'orders/order_list.html', {'orders': orders, 'query': query})

@login_required
def order_create(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        product_ids = request.POST.getlist('product_id[]')
        quantities = request.POST.getlist('quantity[]')
        
        customer = get_object_or_404(Customer, pk=customer_id)
        
        try:
            with transaction.atomic():
                order = Order.objects.create(customer=customer)
                total_amount = Decimal('0.00')
                
                for product_id, qty in zip(product_ids, quantities):
                    if not product_id or not qty:
                        continue
                        
                    qty = int(qty)
                    product = Product.objects.select_for_update().get(pk=product_id)
                    
                    if product.stock < qty:
                        raise ValueError(f"Insufficient stock for {product.name}")
                    
                    # Deduct stock
                    product.stock -= qty
                    product.save()
                    
                    # Create Item
                    item = OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=qty,
                        price=product.price,
                        subtotal=product.price * qty
                    )
                    total_amount += item.subtotal
                
                order.total_amount = total_amount
                order.save()
                
            messages.success(request, 'Order created successfully.')
            return redirect('order_list')
        except ValueError as e:
            # Handle error (basic handling for now)
            error_message = str(e)
            customers = Customer.objects.all()
            products = Product.objects.filter(stock__gt=0)
            return render(request, 'orders/order_form.html', {
                'customers': customers,
                'products': products,
                'error': error_message
            })
            
    customers = Customer.objects.all()
    products = Product.objects.filter(stock__gt=0)
    return render(request, 'orders/order_form.html', {'customers': customers, 'products': products})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

@login_required
def order_pdf(request, pk):
    order = get_object_or_404(Order, pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="order_{order.id}.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter
    
    # Header
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, height - 50, f"Order Receipt #{order.id}")
    
    p.setFont("Helvetica", 12)
    p.drawString(50, height - 80, f"Date: {order.order_date.strftime('%Y-%m-%d %H:%M')}")
    p.drawString(50, height - 100, f"Customer: {order.customer.name}")
    p.drawString(50, height - 120, f"Email: {order.customer.email}")
    
    # Table Header
    y = height - 160
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, "Product")
    p.drawString(300, y, "Price")
    p.drawString(400, y, "Qty")
    p.drawString(500, y, "Subtotal")
    
    # Table Rows
    y -= 20
    p.setFont("Helvetica", 12)
    for item in order.items.all():
        p.drawString(50, y, str(item.product.name))
        p.drawString(300, y, f"${item.price}")
        p.drawString(400, y, str(item.quantity))
        p.drawString(500, y, f"${item.subtotal}")
        y -= 20
    
    # Total
    y -= 20
    p.setFont("Helvetica-Bold", 12)
    p.drawString(400, y, "Total:")
    p.drawString(500, y, f"${order.total_amount}")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
