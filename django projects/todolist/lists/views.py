from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDoList
from .forms import ListForm, ListUpdate

def home(request):
    lists = ToDoList.objects.all()
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
    form = ListForm()
    context = {
        'lists':lists,
        'form':form,
    }
    return render(request, 'lists/lists.html', context)

# def createList(request):
#     if request.method == 'POST':
#         form = ListForm(request.POST)
#         if form.is_valid():
#             form.save()
#     form = ListForm()
#     context = {
#         # 'lists':lists,
#         'form':form,
#     }
#     return render(request, 'lists/add_work.html', context)

def DeleteList(request, pk):
    list = ToDoList.objects.get(id=pk)
    if request.method == 'POST':
        list.delete()
        return redirect('/')
        
    context = {
        'list':list
    }
    return render(request, 'lists/delete.html', context)

def UpdateList(request, pk):
    indi_list = ToDoList.objects.get(id=pk)
    if request.method == 'POST':
        form = ListUpdate(request.POST, instance=indi_list)
        if form.is_valid():
            form.save()

        return redirect('/')
    form = ListUpdate(instance=indi_list)
    context = {
        'indi_list':indi_list,
        'form':form,
    }

    return render(request, 'lists/update.html', context)