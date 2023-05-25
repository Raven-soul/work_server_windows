# Generated by Django 4.2 on 2023-05-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0033_alter_order_sender_email_alter_order_sender_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethodSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Секция метода оплаты')),
            ],
            options={
                'verbose_name': '7. Секция метода оплаты',
                'verbose_name_plural': '7. Секции методов оплаты',
                'ordering': ['id'],
            },
        ),
    ]