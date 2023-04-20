# Generated by Django 4.2 on 2023-04-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0004_delete_new_table_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='infoPages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название страницы')),
                ('path', models.CharField(max_length=255, verbose_name='Путь страницы')),
                ('order', models.IntegerField(verbose_name='Очередь столбца')),
            ],
            options={
                'verbose_name': 'Инфо. страница',
                'verbose_name_plural': 'Инфо. страницы',
                'ordering': ['id'],
            },
        ),
    ]
