# Generated by Django 4.0.1 on 2022-01-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=100)),
                ('mobile_no', models.BigIntegerField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
