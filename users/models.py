from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from ckeditor.fields import RichTextField
# Create your models here.


class Profile(models.Model):
    ACCOUNT_TYPES = (
        ('undergrad', 'Undergraduate'),
        ('grad', 'Graduate'),
        ('invisible', 'Invisible'),
        ('post', 'Postdocs'),
        ('res', 'Research Staff'),
        ('alum', 'Alumni'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default='profiles/default.png')
    username = models.CharField(
        max_length=300, null=True, blank=True, unique=True)
    name = models.CharField(max_length=300, null=True)
    email = models.EmailField(max_length=1000, null=True)
    account_type = models.CharField(max_length=300, null=True,
                                    blank=True, choices=ACCOUNT_TYPES)
    area_of_interest = models.CharField(max_length=300, null=True)
    description = models.TextField(null=True, blank=True)
    skills_and_ongoing_projects = RichTextField(null=True, blank=True)
    cv = models.FileField(
        max_length=300, upload_to='profiles/', null=True, blank=True)
    resume = models.FileField(
        max_length=300, upload_to='profiles/', null=True, blank=True)
    orcid = models.CharField(max_length=300, null=True, blank=True)
    linkedin = models.CharField(max_length=300, null=True, blank=True)
    twitter = models.CharField(max_length=300, null=True, blank=True)
    osf = models.CharField(max_length=300, null=True, blank=True)
    github = models.CharField(max_length=300, null=True, blank=True)
    facebook = models.CharField(max_length=300, null=True, blank=True)
    youtube = models.CharField(max_length=300, null=True, blank=True)
    website = models.CharField(max_length=300, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)


class UserPublications(models.Model):
    DISPLAY_NO = (
        ('display', 'Display'),
        ('noDisplay', 'Do not display'),
    )
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    status_date = models.CharField(max_length=300, null=True, blank=True)
    only_enter_year_xxxx = models.IntegerField(null=True)
    contributors = models.CharField(max_length=1000, null=True, blank=True)
    journal_info = models.CharField(max_length=1000, null=True, blank=True)
    journal_title = models.CharField(max_length=1000, null=True, blank=True)
    pub_link = models.CharField(max_length=500, null=True, blank=True)
    display = models.CharField(
        max_length=300, null=True, blank=True, default='display', choices=DISPLAY_NO)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)


class UserPresentations(models.Model):
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    status_date = models.CharField(max_length=300, null=True, blank=True)
    contributors = models.CharField(max_length=500, null=True, blank=True)
    conference_venue = models.CharField(max_length=500, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)


# class UserSkills(models.Model):
#     author = models.ForeignKey(
#         Profile, on_delete=models.CASCADE, null=True, blank=True)
#     skills = RichTextField(null=True, blank=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True,
#                           primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.skills)


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(user=user,
                                         username=user.username,
                                         email=user.email,
                                         name=user.first_name)


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
