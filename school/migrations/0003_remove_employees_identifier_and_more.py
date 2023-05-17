# Generated by Django 4.1.4 on 2023-05-16 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("school", "0002_alter_employees_options_placework_subject"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employees",
            name="identifier",
        ),
        migrations.RemoveField(
            model_name="employees",
            name="password",
        ),
        migrations.AddField(
            model_name="employees",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
