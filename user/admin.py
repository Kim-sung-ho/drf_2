from django.contrib import admin
from user.models import User
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfileModel)
admin.site.register(HobbyModel)
