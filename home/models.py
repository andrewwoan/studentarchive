from django.db import models
from ckeditor.fields import RichTextField


class HomeText(models.Model):
    home_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.home_text)
