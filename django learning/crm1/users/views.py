from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import Group
from accounts.decorators import unauthenticated_users, user_allowed
from django.contrib.auth.decorators import login_required
from accounts.models import Customer
from accounts.forms import CustomerForm



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user = user
            )
        return redirect('/users/login/')

    form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request, 'users/register.html', context)

@login_required(login_url='user-login')
def user_account(request):
    customer = request.user.customer
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
        return redirect('/user')
    else:
        form = CustomerForm(instance=customer)
    context = {
        'form':form
    }
    
    return render(request, 'users/userAccount.html', context)