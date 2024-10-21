# Generated by Django 5.0.6 on 2024-10-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Комментарии')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата запроса')),
            ],
        ),
    ]
