from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from customers.models import Customer
from products.models import Product
from orders.models import Order
from django.db.models import Sum

class HomeView(TemplateView):
    template_name = 'core/home.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer_count'] = Customer.objects.count()
        context['product_count'] = Product.objects.count()
        context['order_count'] = Order.objects.count()
        context['total_revenue'] = Order.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
        context['recent_orders'] = Order.objects.order_by('-order_date')[:5]
        return context
