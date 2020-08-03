from .models import ToDoList
from django.forms import ModelForm
from django import forms

class ListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ['full_note', 'important']

# class ListUpdate(ModelForm):
#     class Meta:
#         model = ToDoList
#         fields = '__all__'

class ListUpdate(ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'