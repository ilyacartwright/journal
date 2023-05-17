# Generated by Django 4.1.4 on 2023-05-12 05:41

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Positions",
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
                ("name", models.CharField(max_length=50, verbose_name="Название")),
            ],
            options={
                "verbose_name": "Position",
                "verbose_name_plural": "Positions",
            },
        ),
        migrations.AlterField(
            model_name="schools",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None, unique=True, verbose_name="Номер телефона:"
            ),
        ),
    ]
