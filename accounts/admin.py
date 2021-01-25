from django.contrib import admin

# Register your models here.
from accounts.models import Profile, City

admin.site.register(Profile)
admin.site.register(City)