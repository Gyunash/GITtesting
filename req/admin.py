from django.contrib import admin
from .models import Profile
'''
log: basic_admin
pw : basicadmin
'''

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'photo')

admin.site.register(Profile, ProfileAdmin)