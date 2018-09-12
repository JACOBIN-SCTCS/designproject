from django.db import models
import datetime

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




# Create your models here.
class AlmaUser(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60,default='')
    user_email=models.CharField(max_length=40,default='')
    #mobile no
    start_year=models.IntegerField(choices=START_YEAR_CHOICES)
    end_year=models.IntegerField(choices=FINAL_YEAR_CHOICES)
    dept=models.CharField(max_length=8,choices=DEPARTMENT_CHOICES)
    current_pos=models.TextField()

    facebook_url=models.CharField(max_length=70)
    linked_in_url=models.CharField(max_length=70)
    profile_pic=models.ImageField()
    

    def __str__(self):
        return str(self.name)
    