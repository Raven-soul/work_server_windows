# Generated by Django 3.2.18 on 2023-04-18 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0005_category_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='currency',
            field=models.CharField(default='rur', max_length=255, verbose_name='Валюта'),
            preserve_default=False,
        ),
    ]
