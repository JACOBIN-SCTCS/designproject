from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

START_YEAR_CHOICES =[]
for i in range(1995,datetime.datetime.now().year+1):
    START_YEAR_CHOICES.append((i,i))

FINAL_YEAR_CHOICES=[]
for i in range(1999,datetime.datetime.now().year+5):
    FINAL_YEAR_CHOICES.append((i,i))


DEPARTMENT_CHOICES =(
    ('AUTO','AUTO'),
    ('BT','BT'),
    ('CSE','CSE'),
    ('EC','EC'),
    ('MECH','MECH'),
    ('PROD','PROD')
)

TAGS = (
    ('GENERAL', 'GEN'),
    ('EVENT', 'EVENT'),
    ('JOB OFFER' ,'JOB'),

)



# Create your models here.
class AlmaUser(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_obj=models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=60,default='')
    user_email=models.CharField(max_length=40,default='')
    #mobile no
    start_year=models.IntegerField(choices=START_YEAR_CHOICES)
    end_year=models.IntegerField(choices=FINAL_YEAR_CHOICES)
    dept=models.CharField(max_length=8,choices=DEPARTMENT_CHOICES)
    current_pos=models.TextField()

    facebook_url=models.CharField(max_length=70)
    linked_in_url=models.CharField(max_length=70)
    profile_pic=models.ImageField(upload_to='profile_pic',blank=True)


    def __str__(self):
        return str(self.name)


class Events(models.Model):
    event_id=models.AutoField(primary_key=True)
    event_title= models.CharField(max_length=30)
    event_time=models.DateTimeField()
    event_venue=models.CharField(max_length=30)
    event_description=models.TextField()
    event_poster=models.ImageField(upload_to='event_posters',blank=True)
    event_going=models.IntegerField(default=0)

    def __str__(self):
        return self.event_title


class NewsFeed(models.Model):
    post_id=models.AutoField(primary_key=True)
    date_created=models.DateTimeField(default=timezone.now)
    user_id=models.ForeignKey(AlmaUser,on_delete=models.CASCADE)
    tags = models.CharField(choices=TAGS,max_length=10)
    image_url=models.ImageField(blank=True ,upload_to='feed_images')
    post_desc=models.TextField(default='')

    def __str__(self):
        
        return str(self.post_id)


 
class Comments(models.Model):
    cmnt_id=models.AutoField(primary_key=True)
    post_id=models.ForeignKey(NewsFeed,on_delete=models.CASCADE)
    user_id=models.ForeignKey(AlmaUser,on_delete=models.CASCADE)
    cmnt_text=models.TextField(default='')

    def __str__(self):
        return str(self.cmnt_id)
