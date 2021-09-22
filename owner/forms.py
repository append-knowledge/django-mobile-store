from django import forms
from owner.models import Mobile,Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class SignUp(UserCreationForm):
    password1=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['first_name','username','email','password1','password2']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }


class SignIn(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


class AddMobile(ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'

        widgets={
            'company':forms.TextInput(attrs={'class':'form-control'}),
            'model_name':forms.TextInput(attrs={'class':'form-control'}),
            'colour':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'available_pieces': forms.NumberInput(attrs={'class': 'form-control'})

        }
    # company=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # model_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # colour=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    # available_pieces=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    def clean(self):
        cleared_data=super().clean()
        price=cleared_data['price']
        available_pieces=cleared_data['available_pieces']
        model_name=cleared_data['model_name']
        name=Mobile.objects.filter(model_name=model_name)
        if int(price)<0:
            msg='price should be positive'
            self.add_error('price',msg)
        if available_pieces<0:
            msg='should be positive'
            self.add_error('available_pieces',msg)
        if name:
            msg='this model already exist'
            self.add_error('model_name',msg)


class Mobile_update(ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'
        widgets={
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'model_name': forms.TextInput(attrs={'class': 'form-control'}),
            'colour': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'available_pieces': forms.NumberInput(attrs={'class': 'form-control'})

        }


    # company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # model_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # colour = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # available_pieces = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    def clean(self):
        cleared_data=super().clean()
        price =cleared_data['price']
        available_pieces =cleared_data['available_pieces']
        if int(price)<0:
            msg='price should be positive'
            self.add_error('price',msg)
        if available_pieces<0:
            msg='should be positive'
            self.add_error('available_pieces',msg)



class Search_name(forms.Form):
    search= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class MyDashboardEDIT(ModelForm):
    class Meta:
        model=Order
        fields=['status','delivery_date']
        widgets={
            'status':forms.Select(attrs={'class':'form-select'}),
            'delivery_date':forms.DateInput(attrs={'type':'date'})
        }