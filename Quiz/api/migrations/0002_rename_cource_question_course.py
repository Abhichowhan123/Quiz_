# Generated by Django 4.1.1 on 2022-09-29 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='cource',
            new_name='course',
        ),
    ]