# Generated by Django 4.2 on 2023-04-25 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0006_alter_users_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
