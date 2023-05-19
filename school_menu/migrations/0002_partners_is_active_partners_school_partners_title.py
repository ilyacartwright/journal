# Generated by Django 4.1.4 on 2023-05-19 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0003_academicsubjects_alter_positions_options_and_more"),
        ("school_menu", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="partners",
            name="is_active",
            field=models.BooleanField(default=0, verbose_name="Активный?"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="partners",
            name="school",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="settings.schools",
                verbose_name="Школа",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="partners",
            name="title",
            field=models.CharField(
                default=None,
                help_text="Названия пункта выподающего меню",
                max_length=50,
                verbose_name="Название пункта меню",
            ),
            preserve_default=False,
        ),
    ]
