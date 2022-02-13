# Generated by Django 4.0.1 on 2022-01-30 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph_app', '0002_rename_username_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=100)),
                ('mobile_no', models.BigIntegerField()),
            ],
            options={
                'db_table': 'myUser',
            },
        ),
    ]