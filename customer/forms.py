from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from owner.models import Order

class SignUpRegistration(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['first_name','username','email','password1','password2']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})

        }

class LoginForm(forms.Form):
    user_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['products','address','phone_number']
        widgets={
            'products':forms.Select(attrs={'class':'form-control','readonly':True}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'})
        }
