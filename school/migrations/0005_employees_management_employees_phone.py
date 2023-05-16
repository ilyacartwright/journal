# Generated by Django 4.1.4 on 2023-05-16 06:56

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_employees_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='management',
            field=models.BooleanField(blank=True, null=True, verbose_name='Сотрудник может иметь класное руководство?'),
        ),
        migrations.AddField(
            model_name='employees',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Номер телефона:'),
        ),
    ]
