# Generated by Django 3.2.6 on 2021-08-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_userpublications_journal_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpublications',
            name='journal_title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
