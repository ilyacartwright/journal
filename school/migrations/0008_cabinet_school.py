# Generated by Django 4.1.4 on 2023-05-16 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0003_academicsubjects_alter_positions_options_and_more"),
        ("school", "0007_alter_cabinet_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="cabinet",
            name="school",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="settings.schools",
                verbose_name="Школа",
            ),
            preserve_default=False,
        ),
    ]
