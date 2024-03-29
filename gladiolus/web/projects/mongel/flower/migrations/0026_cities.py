# Generated by Django 4.2 on 2023-05-22 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0025_alter_purchasedproducts_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название города')),
            ],
            options={
                'verbose_name': '7. Список доступных городов',
                'verbose_name_plural': '7. Доступные города',
                'ordering': ['id', 'name'],
            },
        ),
    ]
