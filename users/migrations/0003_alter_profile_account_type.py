# Generated by Django 3.2.6 on 2021-08-15 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_undergrad_or_grad_profile_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_type',
            field=models.CharField(blank=True, choices=[('undergrad', 'Undergraduate'), ('grad', 'Graduate'), ('invisible', 'Invisible')], max_length=200, null=True),
        ),
    ]
