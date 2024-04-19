from django.shortcuts import render,redirect
from . models import Items, Drinks
from .forms import AddItemForm, AddDrinkForm , UpdateItemForm
# Create your views here.

def index(request):
    item=Items.objects.all()
    drink = Drinks.objects.all()
    
    menu = {
        'items':item,
        'drinks':drink
    }
    return render(request,'Home/index.html', menu)
#Adding items
def add_item(request):
    form = AddItemForm()
    if request.method =='POST':
        form = AddItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_index')
    return render(request, 'Home/add_item.html',{'form':form})

#Update item
def update_item(request,id):
    items=Items.objects.get(pk=id)
    form = UpdateItemForm(instance=items)
    if request.method =='POST':
        form = UpdateItemForm(request.POST,request.FILES, instance=items)
        if form.is_valid():
            form.save()
            return  redirect('admin_index')
    return render(request,'Home/update_item.html',{'form':form})

#delete item
def delete_item(request, id):
    item = Items.objects.get(pk=id)
    item.delete()
    return redirect('admin_index')
    

#Admin page
def admin_index(request):
    item=Items.objects.all()
    drink = Drinks.objects.all()
    
    menu = {
        'item':item,
        'drink':drink
    }
    return render(request,'Home/admin.html', menu)


        

