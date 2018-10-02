from django.conf.urls import url 
from django.urls import path
from . import views
from .views import AlmaUserCreateView
from django.conf import settings
from django.conf.urls.static import static


app_name='mainapp'

urlpatterns=[

    path('login/' , views.login_user,name='login_user'),
    path('',views.homepage,name='homepage'),
    path('create/',AlmaUserCreateView.as_view(),name='createuser'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/user/',views.userprofileview, name='profile_view'),
    path('logout',views.logout_user,name='logout_user'),
    path('members/',views.AlmaListView,name='list_view'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)