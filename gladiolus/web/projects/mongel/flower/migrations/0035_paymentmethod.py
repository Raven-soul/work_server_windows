# Generated by Django 4.2 on 2023-05-24 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0034_paymentmethodsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Метод оплаты')),
                ('photo', models.ImageField(upload_to='photos/payment/%Y/%m/%d/', verbose_name='Фото')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.paymentmethodsection', verbose_name='Секция')),
            ],
            options={
                'verbose_name': '7. Метод оплаты',
                'verbose_name_plural': '7. Методы оплаты',
                'ordering': ['id'],
            },
        ),
    ]
