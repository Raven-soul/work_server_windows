# Generated by Django 4.2 on 2023-04-20 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0002_new_table_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_table_data',
            name='data2',
            field=models.CharField(default='data', max_length=255, verbose_name='1 часть упаковки'),
            preserve_default=False,
        ),
    ]