from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile, UserPublications, UserPresentations


class updateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'username', 'email', 'name', 'account_type', 'area_of_interest', 'description', 'skills_and_ongoing_projects',
                  'cv', 'resume', 'orcid', 'linkedin', 'twitter', 'osf', 'github',
                  'facebook', 'youtube', 'website', ]


class UserPublicationsForm(ModelForm):
    class Meta:
        model = UserPublications
        fields = ['title', 'status_date',
                  'contributors', 'journal_title', 'journal_info', 'pub_link']
        exclude = ['author']

        def __init__(self, *args, **kwargs):
            super(UserPublicationsForm, self).__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})


class UserPresentationsForm(ModelForm):
    class Meta:
        model = UserPresentations
        fields = ['title', 'status_date', 'contributors', 'conference_venue']
        exclude = ['author']

        def __init__(self, *args, **kwargs):
            super(UserPresentationsForm, self).__init__(*args, **kwargs)
            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})


# class UserSkillsForm(ModelForm):
#     class Meta:
#         model = UserSkills
#         fields = '__all__'
#         exclude = ['author']
