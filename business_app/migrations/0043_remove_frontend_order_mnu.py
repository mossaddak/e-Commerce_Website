# Generated by Django 3.2.3 on 2022-03-08 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0042_frontend_order_mnu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frontend_order',
            name='mNU',
        ),
    ]