from django.conf.urls import url 
from django.urls import path
from . import views
from .views import AlmaUserCreateView


app_name='mainapp'

urlpatterns=[

    path('login/' , views.login_user,name='login_user'),
    path('',views.homepage,name='homepage'),
    path('create/',AlmaUserCreateView.as_view(),name='createuser'),
    path('dashboard/',views.dashboard,name='dashboard')
    
]