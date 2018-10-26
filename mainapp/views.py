from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect,reverse
from django.contrib.auth import logout
from .models import AlmaUser,Events,NewsFeed
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import CreateUserForm,CreatePostForm
from django.db.models import Q
from django.views import View
import json


# Create your views here.
def login_user(request):
    logout(request)
    return render(request,'mainapp/login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('mainapp:login_user'))

def homepage(request):
    #print(request.user.email)
    all_user=AlmaUser.objects.all()
    current_user=all_user.filter(user_email=request.user.email)
    if current_user:
        return redirect('mainapp:dashboard')
    else:

        return redirect('mainapp:createuser')

def dashboard(request):
    user=AlmaUser.objects.get(user_obj=request.user)
    events=Events.objects.all()
    return render(request,'mainapp/dashboard.html', {'user':user , 'events' :events} )


class AlmaUserCreateView(CreateView):

    model=AlmaUser
    #fields =['name','start_year' ,'end_year','dept','current_pos','facebook_url','linked_in_url','profile_pic']
    form_class=CreateUserForm

    template_name_suffix='_createform'
    success_url='/dashboard/'

    def form_valid(self,form):
        model=form.save(commit=False)
        model.user_email=self.request.user.email
        model.user_obj=self.request.user
        image=form.cleaned_data['profile_pic']
        model.profile_pic=image
        model.save()
        return HttpResponseRedirect(self.success_url)



def AlmaListView(request):

    current_user = AlmaUser.objects.get(user_obj=request.user)
    all_users=AlmaUser.objects.all()
    users=all_users
    query=request.GET.get("q")
    if query:

        users=all_users.filter(Q(name__icontains=query) |
        Q(start_year__icontains=query)
        |Q(end_year__icontains=query)
        )
    paginator=Paginator(users,9)
    page=request.GET.get('page')
    userlist=paginator.get_page(page)
    return render(request,'mainapp/display_users.html',{'user':current_user , 'almausers':userlist})




def userprofileview(request):
    current_user = AlmaUser.objects.get(user_obj=request.user)



    #final_users=all_users.exclude(user_obj=request.user)

    return render(request,'mainapp/UserProfile.html',{'user':current_user })


def event_detail(request,pk):
    current_user = AlmaUser.objects.get(user_obj=request.user)
    event =Events.objects.get(event_id=pk)
    return render(request,'mainapp/event_detail.html', {'user':current_user , 'event':event })


def news_feed_page(request):
    all_posts=NewsFeed.objects.all()
    current_user= AlmaUser.objects.get(user_obj=request.user)
    return render(request,'mainapp/newsfeed.html',{'user':current_user, 'posts':all_posts})


    















'''def ajax_going(request):
    if request.is_ajax() and request.POST:
        event_id =request.POST.get('event_id',None)
        event=Events.objects.get(event_id=event_id)
        event.event_going+=1
        event.save()
        message='SUCCESS'
    else:
        message='FAILURE'
    ctx=  { 'message': message}
    return HttpResponse(json.dumps(ctx), content_type='application/json')'''
