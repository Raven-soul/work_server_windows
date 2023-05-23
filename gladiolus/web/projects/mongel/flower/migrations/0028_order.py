# Generated by Django 4.2 on 2023-05-23 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0027_alter_cities_options_alter_user_city_user_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_phone', models.CharField(max_length=255, verbose_name='Телефон отправителя')),
                ('sender_email', models.IntegerField(verbose_name='Email отправителя')),
                ('receiver_name', models.CharField(max_length=255, verbose_name='Имя получателя')),
                ('receiver_phone', models.CharField(max_length=255, verbose_name='Телефон получателя')),
                ('receiver_additional_info', models.CharField(max_length=255, verbose_name='Доп. информация для доставки')),
                ('order_date', models.DateField(verbose_name='Дата заказа')),
                ('order_time', models.TimeField(verbose_name='Время доставки')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('order_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='flower.cities', verbose_name='Город заказа')),
                ('sender_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='flower.user', verbose_name='Данные пользователя')),
            ],
            options={
                'verbose_name': '6. Заказ',
                'verbose_name_plural': '6. Заказы',
                'ordering': ['id'],
            },
        ),
    ]
