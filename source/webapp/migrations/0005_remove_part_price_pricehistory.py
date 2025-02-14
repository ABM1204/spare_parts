# Generated by Django 5.0.6 on 2024-09-13 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0004_alter_user_managers"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="part",
            name="price",
        ),
        migrations.CreateModel(
            name="PriceHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_changed", models.DateTimeField(auto_now_add=True)),
                (
                    "part",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="price_history",
                        to="webapp.part",
                    ),
                ),
            ],
            options={
                "verbose_name": "История цены",
                "verbose_name_plural": "Истории цен",
                "db_table": "price_histories",
                "ordering": ["-date_changed"],
            },
        ),
    ]
