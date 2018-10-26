from django.forms import ModelForm,TextInput
from .models import AlmaUser,NewsFeed
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout ,Row,Div,Field




class CreateUserForm(ModelForm):

     
    
    
    
    class Meta:
        model=AlmaUser
        fields =['name','start_year' ,'end_year','dept','current_pos','facebook_url','linked_in_url','profile_pic']
    
    def __init__(self, *args, **kwargs):
         super(CreateUserForm, self).__init__(*args, **kwargs)
         self.helper=FormHelper(self)
         self.fields['name'].label=False
         self.fields['current_pos'].label=False
         self.fields['facebook_url'].label=False
         self.fields['linked_in_url'].label=False

         self.helper.layout=Layout(

            
                Field( 'name', placeholder="Name "),
               
             
             Div(
           
                Div('start_year',css_class='col-xl-4' ),
                Div('end_year',css_class='col-xl-4'),
                Div('dept',css_class='col-xl-4'),

                css_class='row'
             ),
             Field('current_pos',placeholder="Enter Your current Profession"),
             Field('facebook_url',placeholder="Enter your Facebook profile Link"),
             Field('linked_in_url',placeholder="Enter your linkedIn Profile"),

             'profile_pic'
            
             

         )
   

class CreatePostForm(ModelForm):

    class Meta:
        model=NewsFeed
        fields =['tags','image_url','post_desc']
      
    def __init__(self,*args,**kwargs):
        super(CreatePostForm,self).__init__(*args,**kwargs)
        self.helper=FormHelper(self)
        self.fields['tags'].label=False
        self.fields['image_url'].label=False
        self.fields['post_desc'].label=False

        self.helper.layout= Layout(
            Field('tags'),
            Field('image_url'),
            Field('post_desc',placeholder='Enter Description')

        )
