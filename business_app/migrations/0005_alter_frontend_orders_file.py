# Generated by Django 3.2.3 on 2022-01-11 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0004_rename_frontend_frontend_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontend_orders',
            name='File',
            field=models.FileField(blank=True, null=True, upload_to='file/'),
        ),
    ]