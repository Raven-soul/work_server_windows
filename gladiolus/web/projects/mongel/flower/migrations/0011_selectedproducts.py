# Generated by Django 4.2 on 2023-04-27 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0010_flower_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectedProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество товара')),
                ('sesseion_id', models.CharField(max_length=255, verbose_name='Имя')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.flower', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.user', verbose_name='Пользователь')),
            ],
        ),
    ]