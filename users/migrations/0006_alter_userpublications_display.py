# Generated by Django 3.2.6 on 2021-08-16 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpublications',
            name='display',
            field=models.CharField(blank=True, choices=[('display', 'Display'), ('noDisplay', 'Do not display')], default='display', max_length=200, null=True),
        ),
    ]
