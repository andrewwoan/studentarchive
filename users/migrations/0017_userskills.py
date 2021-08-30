# Generated by Django 3.2.6 on 2021-08-25 23:36

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_profile_account_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSkills',
            fields=[
                ('skills', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
