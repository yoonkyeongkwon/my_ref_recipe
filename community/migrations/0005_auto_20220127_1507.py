# Generated by Django 3.2.5 on 2022-01-27 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_auto_20220126_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
