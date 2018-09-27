from django.forms import ModelForm,TextInput
from .models import AlmaUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout ,Row



class CreateUserForm(ModelForm):

     
    
    
    
    class Meta:
        model=AlmaUser
        fields =['name','start_year' ,'end_year','dept','current_pos','facebook_url','linked_in_url','profile_pic']
    
    def __init__(self, *args, **kwargs):
         super(CreateUserForm, self).__init__(*args, **kwargs)
         self.helper=FormHelper()
         self.helper.layout=Layout(
             'name',
             Row(
                 'start_year',
                 'end_year',
                 'dept'
             ),
             'current_pos',
             'facebook_url',
             'linked_in_url',
             'profile_pic'
             

         )
   

