from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from owner.models import Mobile,Order
from django.contrib import messages
from customer.filters import MobileFilter


# Create your views here.
def sign_up(request):
    form=forms.SignUpRegistration()
    context={}
    context['form']=form
    if request.method=='POST':
        form=forms.SignUpRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customersignin')
        else:
            return render(request,'customer/sign_up.html',{'form':form})


    return render(request,'customer/sign_up.html',context)

def sign_in(request):
    form=forms.LoginForm()
    context={}
    context['form']=form
    if request.method=='POST':
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['user_name']
            password=form.cleaned_data['password']
            user=authenticate(request,username=user_name,password=password)
            if user:
                login(request,user)
                return redirect('home')
        else:
            return render(request,'customer/login.html',{'form':form})


    return render(request,'customer/login.html',context)

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('customersignin')
    else:
        messages.info(request,'you must login first')
        return redirect('customersignin')

def home(request):
    if request.user.is_authenticated:
        mobiles=Mobile.objects.all()
        context={'mobiles':mobiles}
        print(mobiles)

        return render(request,'customer/user.html',context)
    else:
        messages.info(request, 'you must login first')
        return redirect('customersignin')

def order(request,id):
    if request.user.is_authenticated:
        mobiles=Mobile.objects.get(id=id)
        form=forms.OrderForm(initial={'products':mobiles})
        context={'form':form,'mobiles':mobiles}

        if request.method=='POST':
            form=forms.OrderForm(request.POST)
            if form.is_valid():
                order=form.save(commit=False)
                order.user=request.user
                mobiles.available_pieces-=1
                mobiles.save()
                order.save()
                return redirect('home')


        return render(request,'customer/order_conf.html',context)
    else:
        messages.info(request, 'you must login first')
        return redirect('customersignin')

def my_cart(request):
    if request.user.is_authenticated:
        orders=Order.objects.filter(user=request.user).exclude(status='cancel')
        context={'orders':orders}
        return render(request,'customer/cart.html',context)
    else:
        messages.info(request, 'you must login first')
        return redirect('customersignin')

def order_remove(request,id):
    if request.user.is_authenticated:
        order = Order.objects.get(id=id)
        mobile=Mobile.objects.get(id=order.products.id)

        order.status='cancel'
        mobile.available_pieces +=1
        mobile.save()

        order.save()
        return redirect('mycart')
    else:
        messages.info(request, 'you must login first')
        return redirect('customersignin')

def mobile_search(request):
    filters=MobileFilter(request.GET,queryset=Mobile.objects.all())
    return render(request,'customer/mobile_search.html',{'filters':filters})