# Generated by Django 4.2 on 2023-05-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0020_userpages'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sessionUNQid',
            field=models.CharField(max_length=255, null=True, verbose_name='Пользовательский sessionid'),
        ),
    ]
