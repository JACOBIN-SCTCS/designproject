from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect,reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import AlmaUser,Events,JobsIntern,NewsFeed
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import CreateUserForm,CreatePostForm,CreateJobForm
from django.db.models import Q
from django.views import View
import json
import datetime
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def login_user(request):
    logout(request)
    return render(request,'mainapp/index.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('mainapp:homepage'))


@login_required
def homepage(request):
    #print(request.user.email)
    all_user=AlmaUser.objects.all()
    current_user=all_user.filter(user_email=request.user.email)
    if current_user:
        return redirect('mainapp:dashboard')
    else:
        return redirect('mainapp:createuser')

@login_required
def dashboard(request):
    user=AlmaUser.objects.get(user_obj=request.user)
    events=Events.objects.all().order_by('-event_time')
    paginator=Paginator(events,10)
    page=request.GET.get('page')
    display_events=paginator.get_page(page)


    return render(request,'mainapp/dashboard.html', {'user':user , 'events' :display_events} )


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


class AlmaPostCreateView(LoginRequiredMixin,CreateView):

    model=NewsFeed
    form_class=CreatePostForm

    template_name_suffix='_createpostform'

    success_url='/forum/'

    def form_valid(self,form):
        model=form.save(commit=False)
        model.date_created=datetime.datetime.now()
        curuser=AlmaUser.objects.get(user_obj=self.request.user)
        model.user_id=curuser
        model.save()
        return HttpResponseRedirect(self.success_url)




@login_required
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



@login_required
def userprofileview(request):
    current_user = AlmaUser.objects.get(user_obj=request.user)



    #final_users=all_users.exclude(user_obj=request.user)

    return render(request,'mainapp/UserProfile.html',{'user':current_user })

@login_required
def event_detail(request,pk):
    current_user = AlmaUser.objects.get(user_obj=request.user)
    event =Events.objects.get(event_id=pk)
    return render(request,'mainapp/event_detail.html', {'user':current_user , 'event':event })

@login_required
def news_feed_page(request):
    all_posts=NewsFeed.objects.all().order_by('-date_created')
    current_user= AlmaUser.objects.get(user_obj=request.user)

    paginator=Paginator(all_posts,7)
    page=request.GET.get('page')
    post_pages=paginator.get_page(page)
    return render(request,'mainapp/newsfeed.html',{'user':current_user, 'posts':post_pages})

@login_required
def user_detail_view_page(request , user_id):
    current_user = AlmaUser.objects.get(user_obj=request.user)

    try:
        user=AlmaUser.objects.get(user_id=user_id)

        
    
    except AlmaUser.DoesNotExist:
        raise Http404("Invalid User")
    
    return render(request,'mainapp/UserDetails.html',{
        'curuser':current_user,
        'user':user
    })

@login_required
def JobInternView(request):
    
    try:
        all_jobs=JobsIntern.objects.all().order_by('-job_id')
        query=request.GET.get("q")
        if query:
            all_jobs=all_jobs.filter(Q(company_name__icontains=query)
            |
                Q(job_desc__icontains=query)
            )
        paginator=Paginator(all_jobs,6)
        page=request.GET.get('page')
        all_jobs=paginator.get_page(page)
    except:
        all_jobs=None
   
    return render(request,'mainapp/openjobs.html',{'jobs':all_jobs })





class AlmaJobCreateView(LoginRequiredMixin,CreateView):
    model=JobsIntern
    form_class=CreateJobForm
    template_name_suffix='_createform'

    success_url='/jobsoffers/'

    
    def form_valid(self,form):
        model=form.save(commit=False)
        model.save()
        return HttpResponseRedirect(self.success_url)


def UserActivity(request):
    pass








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
