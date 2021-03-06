# Generated by Django 3.2.5 on 2022-01-23 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community_Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_board_id', models.IntegerField()),
                ('title', models.CharField(max_length=45)),
                ('views', models.IntegerField()),
                ('regdate', models.DateTimeField()),
                ('like', models.IntegerField()),
                ('write_id', models.CharField(max_length=45)),
                ('post_like_id', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'community_board',
                'managed': False,
            },
        ),
    ]
