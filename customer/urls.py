from django.urls import path
from customer import views

urlpatterns=[
    path('accounts/signup',views.sign_up,name='customersignup'),
    path('accounts/signin',views.sign_in,name='customersignin'),
    path('accounts/signout',views.signout,name='signout'),
    path('accounts/user',views.home,name='home'),
    path('order/product/<int:id>',views.order,name='orderproduct'),
    path('order/cart',views.my_cart,name="mycart"),
    path('order/cart/remove/<int:id>',views.order_remove,name="removeorder"),
    path('accounts/product/find',views.mobile_search,name='searchmobile')
    ]