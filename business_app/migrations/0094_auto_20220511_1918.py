# Generated by Django 3.2.3 on 2022-05-11 13:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business_app', '0093_auto_20220511_0318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='Likes',
        ),
        migrations.AddField(
            model_name='faq',
            name='likes',
            field=models.ManyToManyField(default=None, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
