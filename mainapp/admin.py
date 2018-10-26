from django.contrib import admin
from .models import AlmaUser,Events,NewsFeed
# Register your models here.

admin.site.register(AlmaUser)
admin.site.register(Events)
admin.site.register(NewsFeed)