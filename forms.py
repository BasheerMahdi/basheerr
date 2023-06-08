from django import forms
from .models import *

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class addCoustmer(UserCreationForm):
  
   
    class Meta:
        model =Coustmer
        fields = {'username','email','password', 'TypeUser'}
        widgets={
           'username':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'password':forms.PasswordInput(attrs={'class':'form-control pull-right'},),
           'email':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'TypeUser':forms.Select(attrs={'class':'form-control pull-right'},),
         }





class addProdect(forms.ModelForm):

    # coustemCatogry=forms.Select(attrs={'class':'form-control pull-right'},)
    class Meta:
        model =Prodect
        fields = ['namepasnes','namescient','manufactureCompany','photo','coustemCatogry','desc','quntity', 'ChoisPrice']
        
        widgets={
           'namepasnes':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'namescient':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'manufactureCompany':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'photo':forms.FileInput(attrs={'class':'form-control pull-right'},),
           'coustemCatogry':forms.Select(attrs={'class':'form-control pull-right'},),
           'desc':forms.TextInput(attrs={'class':'form-control pull-right'},),
           
           'quntity':forms.NumberInput(attrs={'class':'form-control pull-right'},),
           'ChoisPrice':forms.Select(attrs={'class':'form-control pull-right'},),
           

        }

class addSections(forms.ModelForm):
    class Meta:
        model =CoustemSections
        fields = ['name','desc']
        
        widgets={
           'name':forms.TextInput(attrs={'class':'form-control pull-right'},),
           'desc':forms.TextInput(attrs={'class':'form-control pull-right'},),
        }
        

class productOffer(forms.ModelForm):
    class Meta:
        model =productOffers
        fields = ['nameOffers','items_discount']
        
        widgets={
           'nameOffers':forms.TextInput(attrs={'class':'form-control pull-right'},),
           
           'items_discount':forms.NumberInput(attrs={'class':'form-control pull-right'},),
        }