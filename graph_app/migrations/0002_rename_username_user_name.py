# Generated by Django 4.0.1 on 2022-01-23 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='name',
        ),
    ]
