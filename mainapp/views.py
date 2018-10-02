from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect,reverse
from django.contrib.auth import logout
from .models import AlmaUser,Events
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.db.models import Q


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
    user=AlmaUser.objects.get(user_email=request.user.email)
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
    query=request.GET.get("q")
    if query:
        all_users=all_users.filter(Q(name__icontains=query) 
         
         )
    return render(request,'mainapp/display_users.html',{'user':current_user , 'almausers':all_users})


    

def userprofileview(request):
    current_user = AlmaUser.objects.get(user_obj=request.user)
   
     
         
    #final_users=all_users.exclude(user_obj=request.user)

    return render(request,'mainapp/UserProfile.html',{'user':current_user })

  
