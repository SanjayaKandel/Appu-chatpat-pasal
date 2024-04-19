from django import forms
from . models import Items, Drinks

#add Item form
class AddItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields =['image', 'name', 'price', 'description']

#Update item form 
class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields =['image', 'name', 'price', 'description']

#add drink form
class AddDrinkForm(forms.ModelForm):
    class Meta:
        model = Drinks
        fields = ['image', 'name', 'price', 'description']
