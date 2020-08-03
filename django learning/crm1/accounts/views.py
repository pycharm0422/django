from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OrderForm, CustomerForm, UpdateForm
from .filter import OrderFilter
from django.contrib.auth.models import User, Group
from .models import Product, Customer, Order
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_users, user_allowed

def customer(request):
    return render(request, 'accounts/customer.html')

def product(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'accounts/product.html', context)

@login_required(login_url='user-login')
@user_allowed(allowed_user=['admin'])
def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_orders = orders.count()
    order_deliverd = orders.filter(status='Deliverd').count()
    order_pending = orders.filter(status='Pending').count()

    context = {
        'customers':customers,
        'orders':orders,
        'total_orders':total_orders,
        'order_deliverd':order_deliverd,
        'order_pending':order_pending,
    }
    return render(request, 'accounts/dashboard.html', context)

@user_allowed(allowed_user=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    form_filter = OrderFilter(request.GET, queryset = orders)
    orders = form_filter.qs
    total_order = orders.count()
    context = {
        'customer':customer,
        'orders':orders,
        'total_order':total_order,
        'form_filter':form_filter
    }
    return render(request, 'accounts/customer.html', context)

def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateForm(request.POST ,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')    
    form = UpdateForm(instance=customer)
    context = {
        'form':form
    }
    return render(request, 'accounts/update_customer.html', context)


def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboards')
    form = OrderForm(initial={'customer':customer})
    context = {
        'form':form,
    }
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('dashboards')
    form = OrderForm(instance=order)

    context = {
        'form':form
    }

    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'item':order
    }
    return render(request, 'accounts/delete.html', context)


def createCustomer(request):
    if (request.method == "POST"):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    form = CustomerForm()

    context = {
        'form':form
    }
    return render(request, 'accounts/customer_form.html', context)


def userPage(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    order_deliverd = orders.filter(status='Deliverd').count()
    order_pending = orders.filter(status='Pending').count()

    context = {
        'orders':orders,
        'total_orders':total_orders,
        'order_deliverd':order_deliverd,
        'order_pending':order_pending
    }    
    return render(request, 'accounts/user.html', context)