# Generated by Django 4.2 on 2023-04-27 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0009_rename_password_register_form_password_first_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='count',
            field=models.IntegerField(default=10, verbose_name='Количество товара'),
            preserve_default=False,
        ),
    ]