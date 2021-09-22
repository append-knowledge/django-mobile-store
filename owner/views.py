from django.shortcuts import render,redirect
from owner import forms
from owner.models import Mobile,Order
from django.contrib.auth import authenticate,login,logout
from django.db.models import Count


# Create your views here.
def signup(request):
    form=forms.SignUp()
    context={'form':form}
    if request.method=='POST':
        form=forms.SignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')

    return render(request,'signup.html',context)

def signin(request):
    form=forms.SignIn()
    context={'form':form}
    if request.method=='POST':
        form=forms.SignIn(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,'owner_home.html')

            return redirect('addmobile')
    return render(request,'signin.html',context)

def sign_out(request):
    logout(request)
    return render(request,'signin.html')


def addmobile(request):
    form=forms.AddMobile()
    context={'form':form}
    if request.method=='POST':
        form=forms.AddMobile(request.POST,request.FILES)
        context={'form':form}
        if form.is_valid():
            form.save()
            # company=form.cleaned_data['company']
            # model_name=form.cleaned_data['model_name']
            # colour=form.cleaned_data['colour']
            # price=form.cleaned_data['price']
            # available_pieces=form.cleaned_data['available_pieces']
            # mobiles=Mobile(company=company,model_name=model_name,colour=colour,price=price,available_pieces=available_pieces)
            # mobiles.save()
            return redirect('mobilelist')

        else:
            return render(request, 'add_mobile.html', context)
    return render(request,'add_mobile.html',context)


def mobile_list(request):
    form=forms.Search_name()
    mobiles=Mobile.objects.all()
    context={}
    context['mobiles']=mobiles
    context['form']=form
    if request.method=='POST':
        form=forms.Search_name(request.POST,request.FILEDS)
        if form.is_valid():
            search=form.cleaned_data['search']
            mobiles=Mobile.objects.filter(company__contains=search)|Mobile.objects.filter(model_name__contains=search)
            context={'mobiles':mobiles}
            return render(request,'mobile_list.html',context)
    return render(request,'mobile_list.html',context)


def mobile_details(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context['mobile']=mobile
    return render(request,'mobile_details.html',context)

def mobile_delete(request,id):
    mobile=Mobile.objects.get(id=id)
    mobile.delete()
    return redirect('mobilelist')

def mobile_update(request,id):
    mobile=Mobile.objects.get(id=id)
    # data={
    #     'company':mobile.company,
    #     'model_name':mobile.model_name,
    #     'colour':mobile.colour,
    #     'price':mobile.price,
    #     'available_pieces':mobile.available_pieces
    # }
    form=forms.Mobile_update(instance=mobile)
    context={'form':form}

    if request.method=='POST':
        form=forms.Mobile_update(request.POST,instance=mobile,files=request.FILES)
        if form.is_valid():
            # company = form.cleaned_data['company']
            # model_name = form.cleaned_data['model_name']
            # colour = form.cleaned_data['colour']
            # price = form.cleaned_data['price']
            # available_pieces = form.cleaned_data['available_pieces']
            # mobile.company=company
            # mobile.model_name=model_name
            # mobile.colour=colour
            # mobile.price=price
            # mobile.available_pieces=available_pieces
            # mobile.save()
            form.save()
            return redirect('mobilelist')

    return render(request,'mobile_update.html',context)



def my_dashboard(request):
    reports=Order.objects.values("products__model_name").annotate(counts=Count('products')).exclude(status='cancel')
    mobiles=Mobile.objects.all()

    orders=Order.objects.filter(status='ordered')
    context={'orders':orders,'reports':reports,'mobiles':mobiles}

    return render(request,'dashboard.html',context)

def dashedit(request,id):
    form=forms.MyDashboardEDIT()
    order=Order.objects.get(id=id)
    context={'form':form}
    if request.method=='POST':
        form=forms.MyDashboardEDIT(request.POST,instance=order)
        if form.is_valid():
            if order.status == 'cancel':
                mobile=Mobile.objects.get(id=order.products.id)
                mobile.available_pieces +=1
                mobile.save()
            form.save()
            return redirect('dashboard')


    return render(request,'dashedit.html',context)









