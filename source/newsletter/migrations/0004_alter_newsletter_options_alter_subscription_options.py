# Generated by Django 5.0.6 on 2024-11-22 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0003_newsletter"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="newsletter",
            options={"verbose_name": "Рассылка", "verbose_name_plural": "Рассылки"},
        ),
        migrations.AlterModelOptions(
            name="subscription",
            options={"verbose_name": "Подписка", "verbose_name_plural": "Подписки"},
        ),
    ]
