# Generated by Django 3.2.3 on 2022-03-04 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0030_backend_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backend_order',
            old_name='Price',
            new_name='BackendPrice',
        ),
    ]
