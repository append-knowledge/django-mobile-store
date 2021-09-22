from django.urls import path
from owner import views
urlpatterns=[
    path("signup",views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('mobile/add',views.addmobile,name="addmobile"),
    path('mobile/list',views.mobile_list,name='mobilelist'),
    path('mobile/details/<int:id>',views.mobile_details,name='mobiledetails'),
    path('mobile/delete/<int:id>',views.mobile_delete,name='mobiledelete'),
    path('mobile/update/<int:id>',views.mobile_update,name='mobileupdate'),
    path('mobile/logout',views.logout,name='signout'),
    path('',views.my_dashboard,name='dashboard'),
    path('dash/edit/<int:id>',views.dashedit,name='dashedit')

]