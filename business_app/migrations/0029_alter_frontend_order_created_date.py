# Generated by Django 3.2.3 on 2022-03-03 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0028_alter_frontend_order_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontend_order',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
