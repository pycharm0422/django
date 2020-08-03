from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        cartItems = order.total_item
    else:
        items = []
        order = {'total_item':0, 'total_cost':0, 'shipping':False}
        cartItems = order['total_item']
    context = {
        'items':items,
        'order':order,
        'cartItems':cartItems
    }
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'total_item':0, 'total_cost':0, 'shipping':False}
    context = {
        'items':items,
        'order':order
    }
    return render(request, 'store/checkout.html', context)

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,completed=False)
        items = order.orderitem_set.all()
        cartItems = order.total_item

    else:
        items = []
        order = {'total_item':0, 'total_cost':0, 'shipping':False}
        cartItems = order['total_item']

    products = Product.objects.all()

    context = {
        'products':products, 
        'cartItems':cartItems
    }
    return render(request, 'store/store.html', context)

# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    
    order, created = Order.objects.get_or_create(customer=customer, completed=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)