# Generated by Django 3.1.7 on 2021-03-17 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lik',
            old_name='ime',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='lik',
            old_name='prezime',
            new_name='lastname',
        ),
    ]