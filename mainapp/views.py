from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth import logout
from .models import AlmaUser
from django.views.generic.edit import CreateView
from .forms import CreateUserForm


# Create your views here.
def login_user(request):
    logout(request)
    return render(request,'mainapp/login.html')

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
    return render(request,'mainapp/dashboard.html', {'user':user} )


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
    

def UserProfileView(request):
    pass
