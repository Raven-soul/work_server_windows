# Generated by Django 4.2 on 2023-05-04 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0017_rename_email_register_form_email_register_field_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register_form',
        ),
    ]
