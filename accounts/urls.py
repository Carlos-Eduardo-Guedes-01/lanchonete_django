from django.contrib import admin
from django.urls import path
from .views import create, page_login, store, dologin, logouts,page_home,page_info, changepass, changePassword,page_carrinho
name_app='accounts'
urlpatterns=[
    path('admin/',admin.site.urls, name='admin'),
    path('',page_login,name='page_login'),
    path('create/', create,name='/create/'),
    path('home/',page_home,name='page_home'),
    path('perfil/',page_info,name='page_info'),
    path('store/', store,name='/store/'),
    path('dologin/', dologin,name='/dologing/'),
    #path('dashboard/<str:valor>/', dashboard,name='/dashboard/'),
    path('logouts/', logouts,name='/logouts/'),
    path('changepass/', changepass,name='/changepass/'),
    path('changepassword/', changePassword,name='/changepassword/'),
    path('carrinho/',page_carrinho,name='page_carrinho')
]