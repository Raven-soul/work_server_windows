# Generated by Django 4.2 on 2023-05-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0030_order_order_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selectedproducts',
            old_name='order_num',
            new_name='order_code',
        ),
        migrations.AlterField(
            model_name='order',
            name='sender_email',
            field=models.CharField(max_length=255, verbose_name='Email отправителя'),
        ),
    ]
