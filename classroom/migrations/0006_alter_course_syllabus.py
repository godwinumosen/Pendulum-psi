# Generated by Django 4.1.4 on 2023-06-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_alter_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.TextField(),
        ),
    ]