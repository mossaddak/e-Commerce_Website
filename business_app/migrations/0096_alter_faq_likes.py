# Generated by Django 3.2.3 on 2022-05-12 12:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business_app', '0095_alter_faq_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='likes',
            field=models.ManyToManyField(default=None, null=True, related_name='faqLIKES', to=settings.AUTH_USER_MODEL),
        ),
    ]
