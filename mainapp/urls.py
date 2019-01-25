from django.conf.urls import url 
from django.urls import path
from . import views
from .views import AlmaUserCreateView
from .views import AlmaPostCreateView
from .views import AlmaJobCreateView
from django.conf import settings
from django.conf.urls.static import static


app_name='mainapp'

urlpatterns=[
    path('login/' , views.login_user,name='login_user'),
    path('',views.homepage,name='homepage'),
    path('create/',AlmaUserCreateView.as_view(),name='createuser'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard/user/',views.userprofileview, name='profile_view'),
    #path('ajax_going/',views.ajax_going,name='ajax_going'),
    path('logout',views.logout_user,name='logout_user'),
    path('members/',views.AlmaListView,name='list_view'),
    path('dashboard/events/<int:pk>',views.event_detail,name='event_detail'),
    path('forum/',views.news_feed_page,name='forum'),
    path('members/user/<int:user_id>',views.user_detail_view_page,name='users_detail'),
    path('forum/create',AlmaPostCreateView.as_view(),name='createpost'),
    path('jobsoffers/',views.JobInternView,name='openjobs'),
    path('jobsoffers/create',AlmaJobCreateView.as_view(),name='createjob'),

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)