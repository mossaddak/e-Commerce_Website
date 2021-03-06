# Generated by Django 3.2.3 on 2022-05-10 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business_app', '0089_alter_hire_me_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(blank=True, max_length=250, null=True)),
                ('Likes', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='faqLIKE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
