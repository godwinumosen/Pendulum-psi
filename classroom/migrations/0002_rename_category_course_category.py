# Generated by Django 4.1.4 on 2023-06-21 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Category',
            new_name='category',
        ),
    ]
