# Generated by Django 3.2.5 on 2022-01-26 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ref', '0012_auto_20220126_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='rcp_sno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
