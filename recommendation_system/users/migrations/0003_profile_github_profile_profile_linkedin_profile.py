# Generated by Django 5.1.3 on 2025-03-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_about_profile_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github_profile',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_profile',
            field=models.URLField(null=True),
        ),
    ]
