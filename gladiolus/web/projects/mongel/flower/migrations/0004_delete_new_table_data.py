# Generated by Django 4.2 on 2023-04-20 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0003_new_table_data_data2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='new_table_data',
        ),
    ]