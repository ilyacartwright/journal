# Generated by Django 4.1.4 on 2023-05-11 01:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.IntegerField(blank=True, default=0, verbose_name="Возраст"),
        ),
    ]
