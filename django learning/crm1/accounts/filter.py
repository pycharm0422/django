import django_filters
from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        note = django_filters.CharFilter(lookup_expr='icontains')
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']