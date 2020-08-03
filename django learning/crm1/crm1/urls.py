"""crm1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import views as auth_views
from users import views as user_views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.home, name='dashboards'),
    path('product/', auth_views.product, name='products'),
    path('customer/<int:pk>/', auth_views.customer, name='customers'),
    path('create_order/<int:pk>/', auth_views.createOrder, name='create-order'),
    path('update_order/<int:pk>/', auth_views.updateOrder, name='order-update'),
    path('update_form/<int:pk>/', auth_views.updateCustomer, name='update-customer'),
    path('delete_order/<int:pk>/', auth_views.deleteOrder, name='delete'),
    path('create_customer/', auth_views.createCustomer, name='create-customer'),
    path('users/register/', user_views.register, name='user-registration'),
    path('users/login/', LoginView.as_view(template_name='users/login.html'), name='user-login'),
    path('users/logout/', LogoutView.as_view(template_name='users/logout.html'), name='user-logout'),
    path('user/', auth_views.userPage, name='user-page'),
    path('user_account/', user_views.user_account, name='user-account')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)