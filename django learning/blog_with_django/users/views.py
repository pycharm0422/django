from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Profile, Quotes
import random

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} ')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request, 'users/register.html', context)

def profile(request):
    return render(request, 'users/profile.html')

# def quotes(request):
#     quotes = Quotes.objects.all()
#     random_quote = random.choice(quotes)

#     return render(request, 'blog/user_posts')