from django.contrib import admin

# Register your models here.
from .models import Profile, UserPublications, UserPresentations

admin.site.register(Profile)
admin.site.register(UserPublications)
admin.site.register(UserPresentations)
# admin.site.register(UserSkills)
