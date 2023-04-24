# Generated by Django 4.2 on 2023-04-24 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(verbose_name='Оценка товара')),
                ('description', models.TextField(blank=True, verbose_name='Описание отзыва')),
                ('author', models.CharField(max_length=255, null=True, verbose_name='Автор отзыва')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.flower', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['time_create', 'grade'],
            },
        ),
    ]