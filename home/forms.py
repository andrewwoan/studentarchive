from .models import HomeText
from django.forms import ModelForm


class updateForm(ModelForm):
    class Meta:
        model = HomeText
        fields = '__all__'
